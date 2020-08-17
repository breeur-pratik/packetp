#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Venkat Subbiah'
SITENAME = u'Packet Path Blog'
SITEURL = 'http://breeur.in/pelican'
#SITEURL = ""
PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

THEME = 'theme/pelican-theme-bootstrap4'

#Plugins settings
PLUGIN_PATH = ["plugins", "plugin"]
PLUGINS = ['tipue_search','neighbors']

DIRECT_TEMPLATES =  (('index', 'tags', 'categories', 'archives',
                      'authors'))

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

