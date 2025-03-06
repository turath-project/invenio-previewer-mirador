# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
"""Configuration for Invenio-Previewer-Mirador."""

# TODO: This is an example file. Remove it if your package does not use any
# extra configuration variables.

PREVIEWER_MIRADOR_BASE_TEMPLATE = "invenio_previewer_mirador/base.html"
"""Base template for the Mirador previewer."""

PREVIEWER_MIRADOR_TEMPLATE = "invenio_previewer_mirador/mirador_viewer.html"
"""Template for rendering the Mirador viewer."""

PREVIEWER_MIRADOR_JS_URL = "https://unpkg.com/mirador@3.3.0/dist/mirador.min.js"
"""URL for the Mirador JavaScript library."""

PREVIEWER_MIRADOR_CSS_URL = "https://unpkg.com/mirador@3.3.0/dist/mirador.min.css"
"""URL for the Mirador CSS file."""
