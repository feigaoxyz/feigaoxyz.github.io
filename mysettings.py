ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'
# # prevent from generation
# CATEGORY_URL = ''
# # CATEGORY_SAVE_AS = ''
# AUTHOR_URL = ''
# # AUTHOR_SAVE_AS = ''
# TAGS_URL = 'tags/'
# TAGS_SAVE_AS = 'tags/index.html'
# ARCHIVES_URL = 'archives/'
# ARCHIVES_SAVE_AS = 'archives/index.html'
# TAG_URL = 'tag/{slug}/'
# TAG_SAVE_AS = 'tag/{slug}/index.html'

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/README',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README': {'path': 'README.md'},
}

DEFAULT_CATEGORY = 'posts'
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

SUMMARY_MAX_LENGTH = 20

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'toc']

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
    'render_math',
    'cjk-auto-spacing',
]

THEME = ['simple',
         'notmyidea',
         'elegant',
         'themes/mynotmyidea',
         'themes/pelican-bootstrap3',
         ][-1]

# settings for notmyidea theme
# DISQUS_SITENAME = ''
TWITTER_USERNAME = 'feigaochn'
# GITHUB_URL = 'http://github.com/feigaochn'
LINKS = (
    # (Title, URL),
    ('Pelican', 'http://getpelican.com/'),
)
SOCIAL = (
    # (Title, URL),
    ('Weibo', 'http://weibo.com/feigaochn'),
)
MENUITEMS = (
    ('archives', '/archives.html'),
    ('tags', '/tags.html')
)
