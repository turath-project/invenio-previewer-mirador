# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that integrates the Mirador viewer as a previewer for digital objects within the InvenioRDM platform.."""

from .ext import InvenioPreviewerMirador

__version__ = "0.1.0"

__all__ = ("__version__", "InvenioPreviewerMirador")
