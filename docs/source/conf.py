# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ADC Notes'
copyright = '2021, Jacob Wilson'
author = 'Jacob Wilson'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

html_css_files = [
    'css/prism.css',
    'css/override.css',
]

html_js_files = [
    'js/prism.js',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'prev_next_buttons_location' : 'None',
    'show_sphinx' : 'False',
}