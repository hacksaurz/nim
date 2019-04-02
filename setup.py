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
        "click==7.0",
        "Flask==1.0.2",
        "itsdangerous==1.1.0",
        "Jinja2==2.10",
        "MarkupSafe==1.1.1",
        "pluggy==0.9.0",
        "py==1.8.0",
        "six==1.12.0",
        "tox==3.8.4",
        "virtualenv==16.4.3",
        "Werkzeug==0.15.1",
    ],
)
