from invenio_previewer_mirador.ext import InvenioPreviewerMirador


def test_init_app(app):
    assert "invenio-previewer-mirador" in app.extensions


def test_config_loading(app):
    assert "PREVIEWER_MIRADOR_TEMPLATE" in app.config
    assert "PREVIEWER_MIRADOR_JS_URL" in app.config
    assert "PREVIEWER_MIRADOR_CSS_URL" in app.config
