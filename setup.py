#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

tool_name="ntpdos"
version_num = "0.0.1"
author_name = "DaRkReD"
setuptools.setup(name=tool_name,
        version=version_num,
        author=author_name,
        description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/vpnguy/ntpdos",
        packages=setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
        scripts = [
                'core/ntpdos'
            ],
)
