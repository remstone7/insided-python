import os
from setuptools import setup, find_packages

VERSION = '1.0'

setup(
    name='insided',
    version=VERSION,

    packages=find_packages(),
    install_requires=['requests>=2.24.0'],

    url='',
    download_url='',

    author='Remington Stone',
    author_email='remstone7@gmail.com',

    description='Connect Python applications with the InSided API',
    long_description='',
    license='MIT',

    keywords=['insided', 'api',],
)