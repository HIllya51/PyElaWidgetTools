import sys, os
import site

print(sys.version_info.minor)
print(site.getsitepackages())
f = os.path.join(site.getsitepackages()[0], "sipbuild/project.py")
with open(f, "r") as ff:
    x = ff.read()
x = x.replace(
    "yield str(line, encoding=sys.stdout.encoding)",
    "yield str(line, encoding=sys.stdout.encoding, errors='ignore')",
)
with open(f, "w") as ff:
    ff.write(x)


f = os.path.join(site.getsitepackages()[0], "sipbuild/generator/utils.py")
with open(f, "r") as ff:
    x = ff.read()
x = x.replace(
    "zip(td1.types.args, td2.types.args, strict=True):",
    "zip(td1.types.args, td2.types.args):",
)
with open(f, "w") as ff:
    ff.write(x)
