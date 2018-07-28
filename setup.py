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
    name='nim',
    version='1.0',
    description='Web app for playing Nim',
    author='Hacksaurz',
    url='https://github.com/hacksaurz/nim',
    packages=find_packages(exclude=['*.tests']),
    classifiers=CLASSIFIERS,
    install_requires=[
        'click==6.7',
        'Flask==1.0.2',
        'itsdangerous==0.24',
        'Jinja2==2.10',
        'MarkupSafe==1.0',
        'pluggy==0.7.1',
        'py==1.5.4',
        'six==1.11.0',
        'tox==3.1.2',
        'virtualenv==16.0.0',
        'Werkzeug==0.14.1',
    ],
)
