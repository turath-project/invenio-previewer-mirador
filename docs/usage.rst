..
    Copyright (C) 2024 TURATH.

    Invenio-Previewer-Mirador is free software; you can redistribute it
    and/or modify it under the terms of the MIT License; see LICENSE file for
    more details.


Usage
=====

Once Invenio-Previewer-Mirador is installed and configured, it can be used to preview IIIF manifests within your Invenio instance.

Initialization
--------------

The extension is automatically initialized when you import it:

.. code-block:: python

    from invenio_previewer_mirador import InvenioPreviewerMirador

    app = Flask('myapp')
    InvenioPreviewerMirador(app)

Previewing Files
----------------

The Mirador previewer will automatically be used for files that it can preview. The `can_preview` method of the `MiradorPreviewer` class determines whether a file can be previewed.

By default, the previewer is set up to preview IIIF manifests. You may need to adjust the `can_preview` method in `previewer.py` if you want to change this behavior.

Customization
-------------

You can customize the appearance and behavior of the Mirador viewer by modifying the `mirador_viewer.html` template and adjusting the configuration options in your application's config file.

For more advanced customization, you may need to override the `preview` method of the `MiradorPreviewer` class.
