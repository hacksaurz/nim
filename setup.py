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
    # author_email='drunk@yourwedding.com',
    url='https://github.com/hacksaurz/nim',
    packages=find_packages(exclude=['*.tests']),
    classifiers=CLASSIFIERS,
    install_requires=[
        'click==6.7',
        'Flask==1.0',
        'itsdangerous==0.24',
        'Jinja2==2.10',
        'MarkupSafe==1.0',
        'pluggy==0.6.0',
        'py==1.5.3',
        'six==1.11.0',
        'tox==3.0.0',
        'virtualenv==15.2.0',
        'Werkzeug==0.14.1',
    ],
)
