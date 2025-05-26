# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os
import sys

sys.path.insert(0, os.path.abspath(".."))


project = 'SECStreamPy'
copyright = '2025, Peter Mbachu, Rita Chinwendu'
author = 'Peter Mbachu, Rita Chinwendu'
release = '2.0.6'
version = '2.0.6'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    "collapse_navigation": False,
    "display_version": True,
}
# html_logo = "_static/logo-paystackease.png"
# html_favicon = "_static/favicon.png"


latex_engine = 'pdflatex'
latex_element = {
    'papersize': 'letterpaper',
    'pointsize': '14pt',
}
# latex_logo = "_static/logo-paystackease.png"
