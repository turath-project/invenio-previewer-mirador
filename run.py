from flask import Flask, render_template

from invenio_previewer_mirador.config import *
from invenio_previewer_mirador.ext import InvenioPreviewerMirador
from invenio_previewer_mirador.previewer import MiradorPreviewer

app = Flask(
    __name__,
    template_folder="invenio_previewer_mirador/templates",
    static_folder="invenio_previewer_mirador/static",
)

# Load configurations
app.config.from_object("invenio_previewer_mirador.config")

# Initialize the extension
InvenioPreviewerMirador(app)


@app.route("/")
def index():
    # For demonstration, we'll create a dummy file object
    class DummyFile:
        def __init__(self):
            self.uri = "https://iiif.harvardartmuseums.org/manifests/object/299843"

    file = DummyFile()

    if MiradorPreviewer.can_preview(file):
        return MiradorPreviewer.preview(file)
    else:
        return "This file cannot be previewed with Mirador."


if __name__ == "__main__":
    app.run(debug=True)
