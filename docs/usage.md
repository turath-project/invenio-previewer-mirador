# Using Invenio Previewer Mirador

This module provides IIIF manifest and image preview capabilities using Mirador viewer.

## Installation

```bash
pip install invenio-previewer-mirador
```

## Configuration

Add to your `invenio.cfg`:

```python
# Enable Mirador previewer
PREVIEWER_PREFERENCES = ['mirador'] + PREVIEWER_PREFERENCES

# Configure Mirador URLs (optional - defaults shown)
PREVIEWER_MIRADOR_JS_URL = "https://unpkg.com/mirador@3.3.0/dist/mirador.min.js"
PREVIEWER_MIRADOR_CSS_URL = "https://unpkg.com/mirador@3.3.0/dist/mirador.min.css"
```

## Supported Formats

### IIIF Manifests
- Mimetype: application/json
- Must contain IIIF context or manifest type indicators
- Example: 
  ```json
  {
    "@context": "http://iiif.io/api/presentation/2/context.json",
    "@type": "sc:Manifest"
  }
  ```

### Images
- Supported formats: jpg, jpeg, png, gif
- Mimetypes: image/*

## Development

1. Clone the repository:
   ```bash
   git clone https://github.com/turath-project/invenio-previewer-mirador.git
   cd invenio-previewer-mirador
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install in development mode:
   ```bash
   pip install -e .[tests]
   ```

4. Run tests:
   ```bash
   pytest
   ```

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License