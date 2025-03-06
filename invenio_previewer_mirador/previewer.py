# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
"""Mirador previewer for IIIF and image content.

This module provides a previewer implementation for:
- IIIF manifests (application/json)
- Direct image files (image/*)

The previewer uses Mirador viewer for IIIF manifests and a simple
image viewer for direct image files.
"""
import json
from os.path import splitext

import requests
from flask import current_app, render_template


class MiradorPreviewer:
    """Mirador previewer implementation.

    This class provides methods to preview IIIF manifests and image files
    using either Mirador viewer or a simple image preview.
    """

    @staticmethod
    def get_file_content(file):
        """Get the actual content of the file.

        Args:
            file: File object with data attribute containing metadata

        Returns:
            dict: JSON content of the file if successful, None otherwise

        Note:
            This method makes an HTTP request to fetch the file content
            from the URL specified in file.data.links.content
        """
        try:
            if hasattr(file, "data") and isinstance(file.data, dict):
                content_url = file.data.get("links", {}).get("content")
                if content_url:
                    response = requests.get(content_url, verify=False)
                    if response.ok:
                        return response.json()
        except Exception as e:
            print(f"Error getting file content: {str(e)}")
        return None

    @staticmethod
    def can_preview(file):
        """Determine if the given file can be previewed.

        Args:
            file: File object with data attribute containing metadata

        Returns:
            bool: True if file can be previewed, False otherwise

        Supports:
            - IIIF manifests (application/json with IIIF context)
            - Images (image/*)
        """
        if not hasattr(file, "data") or not isinstance(file.data, dict):
            return False

        mimetype = file.data.get("mimetype", "")

        # Handle images
        if mimetype.startswith("image/"):
            return True

        # Handle IIIF manifests
        if mimetype == "application/json":
            try:
                content = MiradorPreviewer.get_file_content(file)
                if content and isinstance(content, dict):
                    return (
                        content.get("@context", "").startswith(
                            "http://iiif.io/api/presentation")
                        or content.get("type") == "Manifest"
                        or content.get("@type") == "sc:Manifest"
                    )
            except Exception as e:
                print(f"Error checking JSON content: {str(e)}")

        return False

    @staticmethod
    def preview(file):
        """Render appropriate template for file preview."""
        try:
            if not hasattr(file, "data") or not isinstance(file.data, dict):
                return "Cannot preview this file", 400

            mimetype = file.data.get("mimetype", "")

            # Handle images
            if mimetype.startswith("image/"):
                ext = splitext(file.data.get("key", ""))[1].lower()[1:]
                format = ext if ext in ["jpg", "jpeg", "png", "gif"] else "jpg"

                return render_template(
                    "invenio_previewer_mirador/simple_image_preview.html",
                    file_url=file.data.get("links", {}).get("content"),
                    format=format,
                )

            # Handle IIIF manifests
            if mimetype == "application/json":
                content_url = file.data.get("links", {}).get("content")
                if content_url:
                    return render_template(
                        "invenio_previewer_mirador/mirador_viewer.html",
                        file=file,  # Pass the entire file object to match template
                        js_url=current_app.config["PREVIEWER_MIRADOR_JS_URL"],
                        css_url=current_app.config["PREVIEWER_MIRADOR_CSS_URL"],
                    )

            return "Cannot preview this file", 400

        except Exception as e:
            print("Error in preview:", str(e))
            raise


mirador_previewer = MiradorPreviewer()
