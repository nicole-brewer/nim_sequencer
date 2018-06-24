# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('nim/nim.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "nim_sequencer",
    packages = ["nim"],
    entry_points = {
        "console_scripts": ['nim = nim.nim:main']
        },
    version = version,
    description = "Command line tool for calculating periodicity in nim sequences."
    long_description = long_descr,
    author = "Nicole Brewer",
    author_email = "brewer36@purdue.edu",
    url = "https://github.com/nicole-brewer/nim_sequencer",
    packages=setuptools.find_packages(),
    # classifiers=(), classifiers can be found at pypi.org/classifiers
)
