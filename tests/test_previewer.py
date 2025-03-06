"""Tests for Mirador previewer."""

import json
from unittest.mock import patch

import pytest
from flask import url_for

from invenio_previewer_mirador.previewer import MiradorPreviewer


class MockFile:
    """Mock file object for testing."""

    def __init__(self, mimetype, content=None, links=None, key=None):
        """Initialize mock file.

        Args:
            mimetype: File mimetype
            content: Optional file content
            links: Optional dict of links
            key: Optional file key/name
        """
        self.data = {
            "mimetype": mimetype,
            "links": links or {},
            "key": key or "test.jpg",
        }
        self.content = content
        self.links = links or {}


@pytest.fixture
def mock_response():
    """Mock successful HTTP response."""

    class MockResponse:
        ok = True

        def json(self):
            return {"@context": "http://iiif.io/api/presentation/2/context.json"}

    return MockResponse()


def test_can_preview_image(app):
    """Test can_preview with image file."""
    file = MockFile(mimetype="image/jpeg")
    assert MiradorPreviewer.can_preview(file) is True


def test_can_preview_iiif(app, mock_response):
    """Test can_preview with IIIF manifest."""
    with patch("requests.get", return_value=mock_response):
        file = MockFile(
            mimetype="application/json",
            links={"content": "http://example.com/manifest.json"},
        )
        assert MiradorPreviewer.can_preview(file) is True


def test_preview_image(app):
    """Test preview with image file."""
    file = MockFile(
        mimetype="image/jpeg",
        links={"content": "http://example.com/image.jpg"},
        key="test.jpg",
    )
    with app.test_request_context():
        response = MiradorPreviewer.preview(file)
        # Check if we get a valid template response
        assert response is not None
        assert isinstance(response, tuple)
        assert len(response) > 0
        # The response should contain the image URL
        assert "http://example.com/image.jpg" in str(response[0])


def test_preview_iiif(app):
    """Test preview with IIIF manifest."""
    file = MockFile(
        mimetype="application/json",
        links={"content": "http://example.com/manifest.json"},
    )
    with app.test_request_context():
        response = MiradorPreviewer.preview(file)
        # Check if we get a valid template response
        assert response is not None
        assert isinstance(response, tuple)
        assert len(response) > 0
        # The response should contain the manifest URL
        assert "http://example.com/manifest.json" in str(response[0])


def test_can_preview_unsupported_file(app):
    """Test can_preview with unsupported file type."""
    file = MockFile(mimetype="text/plain")
    assert MiradorPreviewer.can_preview(file) is False


def test_can_preview_invalid_iiif(app):
    """Test can_preview with invalid IIIF manifest."""

    class MockErrorResponse:
        ok = True

        def json(self):
            return {"invalid": "manifest"}

    with patch("requests.get", return_value=MockErrorResponse()):
        file = MockFile(
            mimetype="application/json",
            links={"content": "http://example.com/manifest.json"},
        )
        assert MiradorPreviewer.can_preview(file) is False


def test_can_preview_network_error(app):
    """Test can_preview with network error."""
    with patch("requests.get", side_effect=Exception("Network error")):
        file = MockFile(
            mimetype="application/json",
            links={"content": "http://example.com/manifest.json"},
        )
        assert MiradorPreviewer.can_preview(file) is False
