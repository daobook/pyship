from pprint import pprint
from setuptools import setup, find_packages

from pyship import __application_name__, __author__, __version__

requirements = ["setuptools", "wheel", "ismain", "balsa", "requests", "attrs", "typeguard", "toml", "pyinstaller", "semver"]

setup(
    name=__application_name__,
    version=__version__,
    author=__author__,

    packages=find_packages(exclude=["test_*"]),

    package_data={
        "": ["pyship.ico"],
    },

    install_requires=requirements
)
