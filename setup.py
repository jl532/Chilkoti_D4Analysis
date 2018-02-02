# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Chilkoti_D4Analysis',
    version='0.1.0',
    description='Distributable copy of the D4 Array Automated Analysis Program',
    long_description=readme,
    author='Jason Liu',
    author_email='JL532@Duke.edu',
    url='https://github.com/jl532',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
