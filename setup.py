from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mpcorbget',

    version='1.0.0',

    description='A tool for observing minor planets'
    long_description=long_description,

    url=''
