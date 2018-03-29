# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

install_requires = [
    'anago',
    'Flask'
]

setup(
    name='anago_webapp',
    version='0.1',
    description='Flask based web application to use anago package',
    long_description=readme,
    author='Kensuke Mitsuzawa',
    author_email='kensuke.mit@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=install_requires,
)