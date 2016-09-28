from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mpcorbget',

    version='1.0.0a1',

    description='A tool for observing minor planets',
    long_description=long_description,

    url='https://github.com/davenporta/mpcorbget',

    author='Alexander Davenport',
    author_email='alexhdavenport@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='astronomy ephemeris ephem minorplanets research',

    packages=find_packages()

    install_requires=['ephem', 'requests'],

    entry_points={
        'console_scripts': [
            'mpcorbget = mpcorbget.__main__:main'
        ]
    },
)
