# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that integrates the Mirador viewer as a previewer for digital objects within the InvenioRDM platform.."""

from setuptools import setup, find_packages

setup(
    name='invenio-previewer-mirador',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'invenio-previewer>=1.0.0',
    ],
    entry_points={
        'invenio_assets.webpack': [
            'mirador_theme = invenio_previewer_mirador.webpack:mirador_theme',
        ],
        'invenio_base.apps': [
            'invenio_previewer_mirador = invenio_previewer_mirador:InvenioPreviewerMirador',
        ],
        # 'invenio_previewer.previewers': [
        #     'mirador = invenio_previewer_mirador.previewer:mirador_previewer',
        # ],
    },
)

