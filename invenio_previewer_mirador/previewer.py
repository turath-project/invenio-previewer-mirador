from invenio_i18n import gettext as _

from . import config


class InvenioPreviewerMirador(object):
    """Invenio-Previewer-Mirador extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        # TODO: This is an example of translation string with comment. Please
        # remove it.
        # NOTE: This is a note to a translator.
        _("A translation string")
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-previewer-mirador"] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "PREVIEWER_MIRADOR_BASE_TEMPLATE",
                app.config["BASE_TEMPLATE"],
            )
        for k in dir(config):
            if k.startswith("PREVIEWER_MIRADOR_"):
                app.config.setdefault(k, getattr(config, k))

# from flask import render_template
# from invenio_previewer.previewers.base import Previewer
#
# class MiradorPreviewer(Previewer):
#     def can_preview(self, file):
#         return file.is_json
#
#     def preview(self, file):
#         return render_template(
#             'invenio_previewer_mirador/preview.html',
#             file=file,
#         )
#
# mirador_previewer = MiradorPreviewer()
