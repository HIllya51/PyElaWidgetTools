"""静态检查 example/ 对绑定 API 的使用是否有效。

- 解析 gen_pyi_from_sip.py 生成的 ElaWidgetTools.pyi，构建 Ela 类的方法/信号/枚举表
- 解析 example/ 全部 .py，追踪变量 -> Ela 类、self -> 所在页面类（含 example 内继承链），
  校验方法/信号/枚举成员是否存在
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

    # 先收集全部文件的类定义（跨文件继承：各页面类都继承自 T_BasePage.py 的 T_BasePage）
    ex_classes = {}
    for path in files:
        tree = ast.parse(open(path, "r", encoding="utf8").read(), filename=path)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                attrs = set()
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        attrs.add(item.name)
                    elif isinstance(item, ast.Assign):
                        for t in item.targets:
                            if isinstance(t, ast.Name):
                                attrs.add(t.id)
                    elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                        attrs.add(item.target.id)
                    elif isinstance(item, ast.ClassDef):
                        attrs.add(item.name)
                bases = [
                    b.id if isinstance(b, ast.Name) else ast.unparse(b) for b in node.bases
                ]
                ex_classes[node.name] = {"attrs": attrs, "bases": bases}

    problems = []
    for path in files:
        tree = ast.parse(open(path, "r", encoding="utf8").read(), filename=path)

        def ela_ancestor(cls_name, depth=0):
            if depth > 10:
                return None
            for b in ex_classes.get(cls_name, {}).get("bases", []):
                if b in short:
                    return short[b]
                r = ela_ancestor(b, depth + 1)
                if r:
                    return r
            return None

        def example_attr(cls_name, attr, depth=0):
            """在 example 类继承链（含 Ela 祖先的 pyi 链 / Qt 基类）中查找属性。"""
            if depth > 10:
                return False
            info = ex_classes.get(cls_name)
            if info is None:
                return False
            if attr in info["attrs"]:
                return True
            for b in info["bases"]:
                if b in ex_classes:
                    if example_attr(b, attr, depth + 1):
                        return True
                elif b in short:
                    if resolve_attr(short[b], attr):
                        return True
                elif qt_base_has(b, attr):
                    return True
            return False

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

        def collect_assigns(node):
            for sub in ast.iter_child_nodes(node):
                collect_assigns(sub)
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
                fn = node.value.func
                if isinstance(fn, ast.Name):
                    for t in node.targets:
                        bind(t, fn.id)
            elif isinstance(node, ast.AnnAssign) and isinstance(node.value, ast.Call):
                fn = node.value.func
                if isinstance(fn, ast.Name):
                    bind(node.target, fn.id)

        collect_assigns(tree)

        # 类名本身可作为静态调用接收者
        for name, info in ex_classes.items():
            if ela_ancestor(name):
                var2cls.setdefault(name, ela_ancestor(name))

        # 3. 带类上下文遍历，校验调用（self.xxx 依据所在 example 类解析）
        def check_calls(node, cls_ctx):
            for stmt in node.body:
                if isinstance(stmt, ast.ClassDef):
                    check_calls(stmt, stmt.name)
                elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    check_calls(stmt, cls_ctx)
                else:
                    for sub in ast.walk(stmt):
                        if isinstance(sub, ast.ClassDef):
                            check_calls(sub, sub.name)
                        if not isinstance(sub, ast.Call):
                            continue
                        func = sub.func
                        if not isinstance(func, ast.Attribute):
                            continue
                        recv = func.value
                        cls_full = None
                        if isinstance(recv, ast.Name):
                            if recv.id == "self" and cls_ctx:
                                # self.attr()：在 example 类链（T_BasePage 等）+ Ela 祖先中查
                                if not example_attr(cls_ctx, func.attr):
                                    problems.append(
                                        f"{path}:{sub.lineno}: '{cls_ctx}.self.{func.attr}' 不存在 ({ast.unparse(sub)[:70]})"
                                    )
                                continue
                            cls_full = var2cls.get(recv.id)
                        elif isinstance(recv, ast.Attribute):
                            cls_full = var2cls.get(ast.unparse(recv))
                        if cls_full and not resolve_attr(cls_full, func.attr):
                            problems.append(
                                f"{path}:{sub.lineno}: '{cls_full}.{func.attr}' 不存在于绑定 ({ast.unparse(sub)[:70]})"
                            )

        check_calls(tree, None)

        # 4. 枚举成员：NS.Enum.MEMBER
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
    print("example 静态检查通过：所有 Ela 类方法/信号/枚举成员均存在于绑定")


if __name__ == "__main__":
    main()
