# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration."""

import os

import pytest
from flask import Flask

from invenio_previewer_mirador import InvenioPreviewerMirador

# Get the path to the templates directory
TEMPLATES_DIR = os.path.join(os.path.dirname(
    os.path.dirname(__file__)), "invenio_previewer_mirador", "templates")


@pytest.fixture(scope="module")
def create_app():
    """Create test app."""
    app = Flask("testapp")
    app.config.update(
        TESTING=True,
        PREVIEWER_MIRADOR_JS_URL=("https://unpkg.com/mirador@3.3.0/dist/mirador.min.js"),
        PREVIEWER_MIRADOR_CSS_URL=("https://unpkg.com/mirador@3.3.0/dist/mirador.min.css"),
    )
    # Add template folder to Flask
    app.template_folder = TEMPLATES_DIR
    return app


@pytest.fixture(scope="module")
def app(create_app):
    """Get app with Mirador previewer."""
    app = create_app
    InvenioPreviewerMirador(app)
    return app


@pytest.fixture
def dummy_file():
    """Dummy file fixture."""

    class DummyFile:
        def __init__(self):
            self.uri = "https://iiif.harvardartmuseums.org/manifests/object/299843"

    return DummyFile()


@pytest.fixture
def mock_iiif_manifest():
    """Return a mock IIIF manifest."""
    return {
        "@context": "http://iiif.io/api/presentation/2/context.json",
        "@type": "sc:Manifest",
        "@id": "https://example.org/manifest.json",
        "label": "Test Manifest",
    }


@pytest.fixture
def mock_image_file():
    """Return a mock image file."""

    class MockImageFile:
        def __init__(self):
            self.uri = "https://example.org/image.jpg"
            self.data = {"mimetype": "image/jpeg", "links": {"content": self.uri}, "key": "test.jpg"}

    return MockImageFile()
