#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import expanduser, join

AUTHOR = 'Jason K. Moore'
SITENAME = 'ENG 122: Intro to Mechanical Vibrations'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
PAGE_ORDER_BY = 'sortorder'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = [join(expanduser("~"), 'src', 'pelican-plugins')]
PLUGINS = ['render_math']
MATH_JAX = {'color':'black'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

STATIC_PATHS = ['materials', 'images']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
