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
        'Flask==0.12.2',
        'itsdangerous==0.24',
        'Jinja2==2.10',
        'MarkupSafe==1.0',
        'pluggy==0.6.0',
        'py==1.5.2',
        'six==1.11.0',
        'tox==2.9.1',
        'virtualenv==15.1.0',
        'Werkzeug==0.14.1',
    ],
)
