# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Episciences Documentation - French'
copyright = 'CC-BY 2022, CCSD'
author = 'Episciences contributors'

release = '0.1'
version = '0.1.0'

html_logo = '_static/episciences.png'
html_css_files = [
    'css/episciences.css',
]
# -- General configuration

html_theme_options = {
    'logo_only': True,
    }

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxext.opengraph',
    'sphinx_panels',

]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
