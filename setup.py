import os
from setuptools import setup, find_packages

VERSION = '1.0.1'

setup(
    name='insided',
    version=VERSION,

    packages=find_packages(),
    install_requires=['requests>=2.24.0'],

    url='https://github.com/remstone7/insided-python',
    download_url='',

    author='Remington Stone',
    author_email='remstone7@gmail.com',

    description='Connect Python applications with the InSided API',
    long_description=(
"""
This is  wrapper around the InSided community forum API.
"""),
    license='MIT',

    keywords=['insided', 'api',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)