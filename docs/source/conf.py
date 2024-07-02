# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PacketLib'
copyright = '2024, Mylo Softworks'
author = 'Mylo Softworks'

release = '1.0.0'
version = release

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs',
    'sphinx.ext.autosectionlabel',
]

sphinx_tabs_disable_tab_closing = True

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
