# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 TURATH.
#
# Invenio-Previewer-Mirador is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_previewer_mirador import InvenioPreviewerMirador


def test_version():
    """Test version import."""
    from invenio_previewer_mirador import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioPreviewerMirador(app)
    assert "invenio-previewer-mirador" in app.extensions

    app = Flask("testapp")
    ext = InvenioPreviewerMirador()
    assert "invenio-previewer-mirador" not in app.extensions
    ext.init_app(app)
    assert "invenio-previewer-mirador" in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert "Welcome to Invenio-Previewer-Mirador" in str(res.data)
