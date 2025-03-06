from invenio_previewer_mirador import config


def test_config_values():
    """Test configuration values."""
    base_template = "invenio_previewer_mirador/base.html"
    viewer_template = "invenio_previewer_mirador/mirador_viewer.html"

    assert config.PREVIEWER_MIRADOR_BASE_TEMPLATE == base_template
    assert config.PREVIEWER_MIRADOR_TEMPLATE == viewer_template
    assert "mirador" in config.PREVIEWER_MIRADOR_JS_URL.lower()
    assert "mirador" in config.PREVIEWER_MIRADOR_CSS_URL.lower()
