# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for previewing files using Mirador IIIF viewer."""

from . import config


class InvenioPreviewerMirador(object):
    """Invenio-Previewer-Mirador extension."""

    def __init__(self, app=None):
        """Extension initialization.

        Args:
            app: The Flask application instance.
        """
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization.

        Args:
            app: The Flask application instance.
        """
        self.init_config(app)
        app.extensions["invenio-previewer-mirador"] = self

    def init_config(self, app):
        """Initialize configuration.

        Args:
            app: The Flask application instance.
        """
        for k in dir(config):
            if k.startswith("PREVIEWER_MIRADOR_"):
                app.config.setdefault(k, getattr(config, k))

    def can_preview(self, file):
        """Determine if the given file can be previewed."""
        from .previewer import mirador_previewer

        return mirador_previewer.can_preview(file)

    def preview(self, file):
        """Preview the given file."""
        from .previewer import mirador_previewer

        return mirador_previewer.preview(file)
