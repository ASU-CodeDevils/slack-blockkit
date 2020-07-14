from setuptools import setup

import slack_blockkit


def readme(file: str):
    with open(file) as f:
        return f.read()


setup(
    version=slack_blockkit.__version__,
    long_description=readme("README.rst")
)
