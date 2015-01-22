#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fei Gao'
SITENAME = u'feigao.me'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    # ('You can add links in your config file', '#'),
    # ('Another social link', '#'),
    ('Twitter', 'https://twitter.com/feigaochn'),
    # ('Facebook', 'https://facebook.com/feigao.chn'),
    # ('Instagram', 'http://instagram.com/feigaochn'),
    # ('LinkedIn', 'http://www.linkedin.com/pub/fei-gao/2b/b36/76a'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'extra',
    'extra/CNAME',
    'extra/README',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README': {'path': 'README.md'},
}

PAGE_PATHS = ['pages']

THEME = ['simple', 'notmyidea'][1]

DEFAULT_CATEGORY = 'posts'
