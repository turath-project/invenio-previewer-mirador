..
    Copyright (C) 2024 TURATH.

    Invenio-Previewer-Mirador is free software; you can redistribute it
    and/or modify it under the terms of the MIT License; see LICENSE file for
    more details.


Configuration
=============

Invenio-Previewer-Mirador can be configured using the following configuration variables:

.. automodule:: invenio_previewer_mirador.config
   :members:

PREVIEWER_MIRADOR_BASE_TEMPLATE
-------------------------------
The base template used for rendering the Mirador previewer.

Default: ``"invenio_previewer_mirador/base.html"``

PREVIEWER_MIRADOR_TEMPLATE
--------------------------
The specific template used for rendering the Mirador viewer.

Default: ``"invenio_previewer_mirador/mirador_viewer.html"``

PREVIEWER_MIRADOR_JS_URL
------------------------
The URL for the Mirador JavaScript library.

Default: ``"https://unpkg.com/mirador@3.3.0/dist/mirador.min.js"``

PREVIEWER_MIRADOR_CSS_URL
-------------------------
The URL for the Mirador CSS file.

Default: ``"https://unpkg.com/mirador@3.3.0/dist/mirador.min.css"``

You can override these settings in your application's configuration file.
