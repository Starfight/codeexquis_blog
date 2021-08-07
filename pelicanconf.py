#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'Flex'

AUTHOR = 'Nicolas Drufin'
SITENAME = 'Code exquis'
SITETITLE = AUTHOR
SITEURL = 'http://localhost:8000/'
SITESUBTITLE = 'Ingénieur DevOps'
SITELOGO = SITEURL + '/images/photo.jpg'
FAVICON = '/images/favicon.ico'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Portfolio', 'https://nicolas.drufin.hackera.fr'),)

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'static']

CUSTOM_CSS = 'static/custom_style.css'

# Mardown extension
# MD_EXTENSIONS = ['extra']

# Code style
PYGMENTS_STYLE = 'monokai'

# Social widget
SOCIAL = (('linkedin', 'http://fr.linkedin.com/pub/nicolas-drufin/'),
          ('github', 'https://github.com/Starfight/'),
          ('facebook', 'http://www.facebook.com/nicolas.drufin'),
          ('twitter', 'https://twitter.com/Magikhaos'),
          ('envelope', 'mailto:nicolas.drufin@hackera.fr'),
          ('rss', '/feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MAIN_MENU = True

# Enable i18n plugin, probably you already have some others here.
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Default theme language.
I18N_TEMPLATES_LANG = 'en'
# Your language.
DEFAULT_LANG = 'fr'
OG_LOCALE = 'fr_FR'
LOCALE = ('fr_FR.utf8', 'fr')

DEFAULT_DATE_FORMAT = '%-d %B %Y'
