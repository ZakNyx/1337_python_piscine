from setuptools import setup, find_packages

"""
Setup script for the 'ft_package' Python package.

This script uses setuptools to define the
package configuration and metadata.
It creates a distributable version of the
package that can be installed via pip.

Attributes
----------
name : str
    The name of the package.
    This is the identifier under which the package will be installed.
version : str
    The version of the package.
    This should follow semantic versioning (e.g., '0.0.1').
author : str
    The name of the author of the package.
author_email : str
    The email address of the author, provided for contact purposes.
url : str
    The URL of the project's homepage or repository.
description : str
    A short summary of what the package does.
packages : list
    A list of all Python import packages that should
    be included in the distribution package.
classifiers : list
    A list of classifiers that categorize the package.
    These help others find the package in package indexes.
entry_points : dict
    Entry points allow the creation of command-line tools
    that users can run directly. Currently, this is empty.

Usage
-----
To build the package, run:
    $ python setup.py sdist bdist_wheel

To install the package locally, use:
    $ pip install ./dist/ft_package-0.0.1.tar.gz

To display package information after installation:
    $ pip show -v ft_package

To uninstall the package:
    $ pip uninstall ft_package
"""

setup(
    name='ft_package',
    version='0.0.1',
    author='zihirri',
    author_email='zihirri@student.1337.ma',
    url="https://github.com/ZakNyx/1337_python_piscine/tree/main/day00/ex09",
    description='A sample test package',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [],
    },
)
