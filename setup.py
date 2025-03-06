# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that integrates the Mirador viewer."""

from setuptools import find_packages, setup

setup(
    name="invenio-previewer-mirador",
    version="0.1.0",
    description=__doc__,
    long_description=open("README.rst").read(),
    keywords="invenio previewer mirador iiif",
    license="MIT",
    author="TURATH",
    author_email="info@turath.org",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_base.apps": [
            "invenio_previewer_mirador = invenio_previewer_mirador:InvenioPreviewerMirador",
        ],
        "invenio_previewer.previewers": ["mirador = invenio_previewer_mirador.previewer:mirador_previewer"],
    },
    install_requires=[
        "invenio-previewer>=1.3.6",
        "Flask>=1.0.4",
        "requests>=2.25.0",
    ],
    extras_require={
        "docs": [
            "Sphinx>=3.0.0",
        ],
        "tests": [
            "pytest>=6.0.0",
            "pytest-invenio>=1.4.0",
            "pytest-cov>=2.10.1",
            "pytest-mock>=3.3.1",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
