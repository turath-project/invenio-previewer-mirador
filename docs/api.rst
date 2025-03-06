..
    Copyright (C) 2024 TURATH.

    Invenio-Previewer-Mirador is free software; you can redistribute it
    and/or modify it under the terms of the MIT License; see LICENSE file for
    more details.


API Docs
========

This section provides detailed information about the API of Invenio-Previewer-Mirador.

Extension
---------

.. automodule:: invenio_previewer_mirador.ext
   :members:

The extension module contains the main `InvenioPreviewerMirador` class, which initializes the module and registers it with the Flask application.

Previewer
---------

.. automodule:: invenio_previewer_mirador.previewer
   :members:

The previewer module defines the `MiradorPreviewer` class, which handles the logic for determining if a file can be previewed and rendering the preview.

Config
------

.. automodule:: invenio_previewer_mirador.config
   :members:

This module contains all the configuration options for Invenio-Previewer-Mirador, including URLs for Mirador JavaScript and CSS files, and template paths.

