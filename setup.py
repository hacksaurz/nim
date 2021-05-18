#!/usr/bin/env python
from setuptools import find_packages, setup

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Web Environment",
    "Framework :: Flake8",
    "Framework :: Flask",
    "Framework :: Pytest",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: JavaScript",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Games/Entertainment :: Board Games",
]

setup(
    name="nim",
    version="1.0",
    description="Web app for playing Nim",
    author="Hacksaurz",
    url="https://github.com/hacksaurz/nim",
    packages=find_packages(exclude=["*.tests"]),
    classifiers=CLASSIFIERS,
    install_requires=[
        "click==8.0.0",
        "Flask==2.0.0",
        "itsdangerous==2.0.0",
        "Jinja2==3.0.0",
        "MarkupSafe==2.0.0",
        "pluggy==0.13.1",
        "py==1.10.0",
        "six==1.16.0",
        "tox==3.23.1",
        "virtualenv==20.4.6",
        "Werkzeug==2.0.1",
    ],
)
