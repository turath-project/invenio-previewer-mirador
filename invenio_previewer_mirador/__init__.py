# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for previewing files using Mirador IIIF viewer."""

try:
    from .version import __version__
except ImportError:
    __version__ = "0.1.0"

from .ext import InvenioPreviewerMirador

__all__ = ("__version__", "InvenioPreviewerMirador")
