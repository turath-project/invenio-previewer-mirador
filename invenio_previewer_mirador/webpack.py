from invenio_assets.webpack import WebpackBundle

mirador_theme = WebpackBundle(
    __name__,
    'assets',
    entry={
        'semantic-ui': './js/customPreviewers.js',
    },
    dependencies={
        'mirador': '^3.0.0',
    },
    devDependencies={
    },
)

bundles = {
    'semantic-ui': mirador_theme,
}

