import os
import sys

# Add project path
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'Manage Automatically'
author = 'Cynthia Mailman'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output -------------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ✅ Bing Verification Meta Tag (Correct Way)
html_meta = {
    "google-site-verification": "dZOmni4YZ1ml8KZCOoU6Psuofz7m1UJjcT1TiyIeto4"
}

# Optional: Add custom CSS or JS (if needed)
html_css_files = []
html_js_files = []

# -- Options for internationalization ----------------------------------------
language = 'en'

# -- Misc settings -----------------------------------------------------------
master_doc = 'index'