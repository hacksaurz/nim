#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='nim',
    version='1.0',
    description='Web app for playing Nim',
    author='Hacksaurz',
    #author_email='drunk@yourwedding.com',
    url='https://github.com/hacksaurz/nim',
    packages=find_packages(exclude=['*.tests']),
    install_requires=[
        'click==6.7',
        'Flask==0.12.2',
        'itsdangerous==0.24',
        'Jinja2==2.10',
        'MarkupSafe==1.0',
        'pluggy==0.6.0',
        'py==1.5.3',
        'six==1.11.0',
        'tox==2.9.1',
        'virtualenv==15.2.0',
        'Werkzeug==0.14.1',
    ],
)
