from setuptools import setup, find_packages, Distribution, Command
import sys, platform

bindingfor = sys.argv[-1]
sys.argv.pop(-1)

bit = sys.argv[-1]
sys.argv.pop(-1)


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


if bindingfor == "PyQt5":
    req = "PyQt5"  # >=5.15
elif bindingfor == "PyQt6":
    req = "PyQt6"  # >=6.7
elif bindingfor == "PySide6":
    req = "PySide6"

setup(
    name=f"{bindingfor}-ElaWidgetTools",
    version="0.0.5",
    author="HIllya51",
    license="MIT",
    install_requires=[f"""{bindingfor}"""],
    packages=find_packages(include=[f"{bindingfor}ElaWidgetTools"]),
    include_package_data=False,
    package_data={
        f"{bindingfor}ElaWidgetTools": ["*.pyd"],
    },
    distclass=BinaryDistribution,
    options={
        "bdist_wheel": {
            "py_limited_api": ["cp38", "cp37"][bindingfor == "PyQt5"],
            "plat_name": ("win32", "win_amd64")[bit == "64"],
        }
    },
    project_urls={
        "Homepage": "https://github.com/HIllya51/PyElaWidgetTools",
        "Repository": "https://github.com/HIllya51/PyElaWidgetTools",
    },
)
