#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'Flex'

AUTHOR = 'Nicolas Drufin'
SITENAME = 'Code exquis'
SITEURL = ''
SITESUBTITLE = 'Ingénieur Big Data & UX'
SITELOGO = SITEURL + '/images/dcns.jpg'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'static']

CUSTOM_CSS = 'static/custom_style.css'

# Mardown extension
# MD_EXTENSIONS = ['extra']

# Social widget
SOCIAL = (('linkedin', 'http://fr.linkedin.com/pub/nicolas-drufin/'),
          ('github', 'https://github.com/Starfight/'),
          ('facebook', 'http://www.facebook.com/nicolas.drufin'),
          ('twitter', 'https://twitter.com/Magikhaos'),
          ('envelope-o', 'mailto:nicolas.drufin@ensc.fr'),
          ('rss', '/feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MAIN_MENU = True

# Enable i18n plugin, probably you already have some others here.
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

# Default theme language.
I18N_TEMPLATES_LANG = 'en'
# Your language.
DEFAULT_LANG = 'fr'
OG_LOCALE = 'fr_FR'
LOCALE = 'fr'
