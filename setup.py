from setuptools import setup


setup(
    name="weChat-python-sdk",
    version='1.0',
    description="Python wrapper for weChat API",
    author="Vincent Ting",
    author_email="pro@vincenting.com",
    packages=['weChat'],
    install_requires=["poster >= 0.8.1"],
    )
