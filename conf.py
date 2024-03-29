# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = 'Aide Memoire'
copyright = '2022, rmarasigan'
author = 'Shanelle Marasigan'

# The short X.Y version
version = '1'
# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------
# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'myst_parser'
]

# Enable myst extenstion
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "html_image",
    "replacements"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.gitignore',
    'venv',
    '.go'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Set link name generated in the top bar.
# html_title = 'Aide Memoire 👩🏻‍💻'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # Set the logo icon.
    'html_logo': '&#xe31f',

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Aide Memoire 👩🏻‍💻',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/rmarasigan/notes',
    'repo_name': 'Notes',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    # 'base_url': 'https://rmarasigan.github.io/aide-memoire',

    # The theme color for mobile browsers
    'theme_color': '263238',

    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'light-blue',

    # Visible levels of the global TOC; -1 means unlimited
    # 'globaltoc_depth': 2,

    # If False, expand all TOC entries
    # 'globaltoc_collapse': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    "**": ["logo-text.html", "localtoc.html", "searchbox.html"]
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Notesdoc'


# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'Notes.tex', 'Notes', 'Shanelle Marasigan', 'manual')]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'notes', 'Reference (Network, Programming, etc.)', [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(master_doc, 'Notes', 'Notes', author, 'Notes', 'Reference (Network, Programming, etc.)', 'Miscellaneous')]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------