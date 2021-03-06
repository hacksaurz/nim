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
        "Flask==1.1.1",
        "itsdangerous==1.1.0",
        "Jinja2==2.11.1",
        "MarkupSafe==1.1.1",
        "pluggy==0.13.1",
        "py==1.8.1",
        "six==1.14.0",
        "tox==3.14.3",
        "virtualenv==16.7.9",
        "Werkzeug==1.0.0",
    ],
)
