#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="weibo-ng",
    version="0.3.0",
    description="Python sina weibo sdk",
    author="Lx Yu",
    author_email="i@lxyu.net",
    py_modules=["weibo",],
    url="http://lxyu.github.io/weibo/",
    license="BSD",
    long_description=open("README.rst").read(),
    install_requires=["requests>=2.10.0",],
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
