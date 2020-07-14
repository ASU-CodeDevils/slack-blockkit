import codecs
import os
import re
from setuptools import setup, find_packages

from src import slack_blockkit

def readme(file: str):
    with open(file) as f:
        return f.read()


setup(
    version=slack_blockkit.__version__,
    long_description=readme("README.rst")
)
