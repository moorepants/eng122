#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

AUTHOR = 'Jason K. Moore'
SITENAME = 'ENG 122: Intro to Mechanical Vibrations'
SITEURL = ''
SOURCEURL = 'http://github.com/moorepants/eng122'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# This sets the default pages to be top level items.
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_ORDER_BY = 'sortorder'
STATIC_PATHS = ['scripts']

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

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

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

## THEME

# Alchemy theme settings
SITESUBTITLE = ''
SITEIMAGE = ''
DESCRIPTION = ''
PYGMENTS_STYLE = 'emacs'
