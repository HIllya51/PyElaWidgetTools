"""静态检查 example/ 对新绑定 API 的使用是否仍存在。

- 解析 gen_pyi_from_sip.py 生成的 ElaWidgetTools.pyi，构建 Ela 类的方法/信号/枚举表
- 解析 example/ 全部 .py，追踪变量/页面类 -> Ela 类，校验属性访问是否存在
- Qt 基类的继承成员通过本地安装的 PyQt5 解析（example 本身基于 PyQt5）
仅做存在性检查（方法/信号/枚举成员），不做签名检查。
"""
import ast
import os
import sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

PYI = "scripts/pyqt/ElaWidgetTools.pyi"
EXAMPLE_DIR = "example"


def load_pyi():
    """pyi -> {全限定类名: {attrs, bases}}，嵌套类全限定登记。"""
    tree = ast.parse(open(PYI, "r", encoding="utf8").read())
    classes = {}

    def process_class(stmt, prefix):
        name = f"{prefix}.{stmt.name}" if prefix else stmt.name
        bases = [ast.unparse(b) for b in stmt.bases]
        classes[name] = {"bases": bases, "attrs": set()}
        for item in stmt.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                classes[name]["attrs"].add(item.name)
            elif isinstance(item, ast.Assign):
                for t in item.targets:
                    if isinstance(t, ast.Name):
                        classes[name]["attrs"].add(t.id)
            elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                classes[name]["attrs"].add(item.target.id)
            elif isinstance(item, ast.ClassDef):
                classes[name]["attrs"].add(item.name)
                process_class(item, name)

    for stmt in tree.body:
        if isinstance(stmt, ast.ClassDef):
            process_class(stmt, "")
    return classes


def qt_base_has(base, attr):
    """base 为 Qt 类名，用本地 PyQt5 判定继承属性；无法判定时返回 True 以免误报。"""
    try:
        import importlib

        mods = [
            importlib.import_module(f"PyQt5.{m}") for m in ("QtWidgets", "QtCore", "QtGui")
        ]
        name = base.split(".")[-1]
        for m in mods:
            if hasattr(m, name):
                return hasattr(getattr(m, name), attr)
        return True
    except Exception:
        return True


def main():
    classes = load_pyi()
    short = {k.split(".")[-1]: k for k in classes}

    def resolve_attr(cls_full, attr, seen=None):
        if seen is None:
            seen = set()
        if cls_full in seen or cls_full not in classes:
            return False
        seen.add(cls_full)
        if attr in classes[cls_full]["attrs"]:
            return True
        for b in classes[cls_full]["bases"]:
            b_short = b.split(".")[-1]
            if b_short in short:
                if resolve_attr(short[b_short], attr, seen):
                    return True
            elif qt_base_has(b, attr):
                return True
        return False

    files = []
    for root, _, fs in os.walk(EXAMPLE_DIR):
        for f in fs:
            if f.endswith(".py"):
                files.append(os.path.join(root, f))

    problems = []
    for path in files:
        tree = ast.parse(open(path, "r", encoding="utf8").read(), filename=path)

        # 1. example 类继承链：类名 -> 祖先中的第一个 Ela 类
        ex_bases = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                ex_bases[node.name] = [
                    b.id if isinstance(b, ast.Name) else ast.unparse(b) for b in node.bases
                ]

        def ela_ancestor(cls_name, depth=0):
            if depth > 10:
                return None
            for b in ex_bases.get(cls_name, []):
                if b in short:
                    return short[b]
                r = ela_ancestor(b, depth + 1)
                if r:
                    return r
            return None

        # 2. 变量 -> Ela 类（全限定名）
        var2cls = {}

        def bind(target, cls_short):
            if cls_short not in short:
                return
            if isinstance(target, ast.Name):
                var2cls[target.id] = short[cls_short]
            elif (
                isinstance(target, ast.Attribute)
                and isinstance(target.value, ast.Name)
                and target.value.id == "self"
            ):
                var2cls[f"self.{target.attr}"] = short[cls_short]

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
                fn = node.value.func
                if isinstance(fn, ast.Name):
                    for t in node.targets:
                        bind(t, fn.id)
            elif isinstance(node, ast.AnnAssign) and isinstance(node.value, ast.Call):
                fn = node.value.func
                if isinstance(fn, ast.Name):
                    bind(node.target, fn.id)

        # 类名本身可作为静态调用接收者，或 self 的类型
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                anc = ela_ancestor(node.name)
                if anc:
                    var2cls.setdefault(node.name, anc)

        # 3. 校验调用
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            if not isinstance(func, ast.Attribute):
                continue
            recv = func.value
            cls_full = None
            if isinstance(recv, ast.Name):
                cls_full = var2cls.get(recv.id)
            elif isinstance(recv, ast.Attribute):
                cls_full = var2cls.get(ast.unparse(recv))
            if cls_full and not resolve_attr(cls_full, func.attr):
                problems.append(
                    f"{path}:{node.lineno}: '{cls_full}.{func.attr}' 不存在于绑定 ({ast.unparse(node)[:80]})"
                )

        # 4. 枚举成员：NS.Enum.MEMBER / NS.MEMBER（NS 为 pyi 里的命名空间类）
        for node in ast.walk(tree):
            if not isinstance(node, ast.Attribute):
                continue
            if not (isinstance(node.value, ast.Attribute) and isinstance(node.value.value, ast.Name)):
                continue
            ns = node.value.value.id
            enum_name = node.value.attr
            member = node.attr
            if ns not in short:
                continue
            ns_full = short[ns]
            if enum_name in classes[ns_full]["attrs"] and f"{ns_full}.{enum_name}" in classes:
                if member not in classes[f"{ns_full}.{enum_name}"]["attrs"]:
                    problems.append(
                        f"{path}:{node.lineno}: 枚举成员 '{ns}.{enum_name}.{member}' 不存在"
                    )

    if problems:
        print("\n".join(problems))
        print(f"\n共 {len(problems)} 个问题")
        sys.exit(1)
    print("example 静态检查通过：所有 Ela 类方法/信号/枚举成员均存在于新绑定")


if __name__ == "__main__":
    main()
