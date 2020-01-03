#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

AUTHOR = 'Jason K. Moore'
SITENAME = 'ENG 122: Intro to Mechanical Vibrations'
SITEURL = ''
SOURCEURL = 'http://github.com/moorepants/eng122'

PATH = 'content'
PAGE_ORDER_BY = 'sortorder'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

try:
    with open('local-config.yml', 'r') as config_file:
        config_data = yaml.load(config_file)
except IOError:
    THEME = ''
    PLUGIN_PATHS = ''
else:
    THEME = config_data['THEME_PATH']
    PLUGIN_PATHS = config_data['PLUGIN_PATHS']

PLUGINS = ['render_math']
MATH_JAX = {'color': 'black'}

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
