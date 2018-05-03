#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Octa9on'
SITENAME = u'Weweiti Foosun Chuuk'
SITEURL = 'http://chuuk.octa9on.net'

THEME = '/var/www/html/chuuk/themes/blueidea'
#THEME = '/var/www/html/chuuk/themes/notmyidea'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/favicon.ico', 'extra/square-chuuk-144.png']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/square-chuuk-144.png': {'path': 'square-chuuk-144.png'},
}

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'English'

DISQUS_SITENAME = "chuuk"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CACHE_PATH = '/var/www/html/chuuk/cache'
CHECK_MODIFIED_METHOD = 'mtime'
