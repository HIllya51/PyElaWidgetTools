from setuptools import setup, find_packages, Distribution, Command
import sys, platform


QtVer = "6"

if sys.argv[-1] == "5":
    QtVer = "5"
    sys.argv.pop(-1)

bit = "64"

if sys.argv[-1] == "32":
    bit = "32"
    sys.argv.pop(-1)


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


setup(
    name=f"PyQt{QtVer}-ElaWidgetTools",
    version="0.0.4",
    author="HIllya51",
    license="MIT",
    install_requires=[f"""{['PyQt6>=6.7','PyQt5>=5.15'][QtVer=="5"]}"""],
    packages=find_packages(include=[f"PyQt{QtVer}ElaWidgetTools"]),
    include_package_data=False,
    package_data={
        f"PyQt{QtVer}ElaWidgetTools": ["*.pyd"],
    },
    distclass=BinaryDistribution,
    options={
        "bdist_wheel": {
            "py_limited_api": ["cp38", "cp37"][QtVer == "5"],
            "plat_name": ("win32", "win_amd64")[bit == "64"],
        }
    },
    project_urls={
        "Homepage": "https://github.com/HIllya51/PyElaWidgetTools",
        "Repository": "https://github.com/HIllya51/PyElaWidgetTools",
    },
)
