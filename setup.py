import os
from setuptools import Command, setup, find_packages

from src.app.tools.app_tool import AppTool


class CleanCommand(Command):
    user_options = []

    @staticmethod
    def run():
        os.system("rm -vrf ./build `find -type d -name *egg-info` `find -type d -name __pycache__`")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


with open("README.md") as f:
    README = f.read()

with open("LICENSE") as f:
    LICENSE = f.read()

setup(
    name="app",
    version=AppTool.VERSION,
    description="Application for the whatever at wherever.",
    long_description=README,
    author="Christopher Behrens, Christopher Passow",
    author_email="christopher.behrens@desy.de, christopher.passow@desy.de",
    url="https://github.com/chrisbpoint/the-app",
    license=LICENSE,
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={"app": ["resources/app.png"]},
    install_requires=["pyqt", "pyqtgraph", "doocspie", "numpy>=1.11"],
    scripts=["bin/app"],
    cmdclass={"clean": CleanCommand}
)
