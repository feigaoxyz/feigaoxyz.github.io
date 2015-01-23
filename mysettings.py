ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/README'
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README': {'path': 'README.md'},
}

# DEFAULT_CATEGORY = 'posts'
USE_FOLDER_AS_CATEGORY = False

DEFAULT_DATE_FORMAT = '%Y-%m-%d %a'

# SUMMARY_MAX_LENGTH = 20

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'toc']

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
    'render_math',
    'cjk-auto-spacing',
]


THEME = 'themes/pelican-bootstrap3'

########################################
# pelican-bootstrap3 settings

# honors standard settings
DISPLAY_CATEGORIES_ON_MENU = False
# MENUITEMS = (
    # ('archives', '/archives.html'),
    # ('tags', '/tags.html')
# )
LINKS = (
    # (Title, URL),
    ('Pelican', 'http://getpelican.com/'),
)

# set in publishconf.py
# DISQUS_SITENAME
# GOOGLE_ANALYTICS

# BOOTSTRAP_THEME: http://bootswatch.com
# name from bootstrap.{theme-name}.min.css
BOOTSTRAP_THEME = ['spacelab',
                   'readable',
                   'paper',
                   'simplex'][2]

# Article info
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = True

# Custom CSS
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = STATIC_PATHS + ['extra/custom.css']
EXTRA_PATH_METADATA['extra/custom.css'] = {'path': 'static/custom.css'}

# Pygments
PYGMENTS_STYLE = 'solarizedlight'

# Site Brand
# SITELOGO = 'images/site_logo.png'
# SITELOGO_SIZE = '150'

# Breadcrumbs
DISPLAY_BREADCRUMBS = True

# Favicon
FAVICON = '/images/fav.jpg'

# Index page
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Short menu labels for pages
# set 'Menulabel:' in page header

# About Me
# ABOUT_ME = "I'm <b>Fei Gao</b>."
# AVATAR = '/images/fav.jpg'

# Banner
# BANNER = '/path/to/banner.png'
# BANNER_SUBTITLE = 'This is my subtitle'
# BANNER_ALL_PAGES = True

# Sidebar
SOCIAL = (
    # (Title, URL),
    ('twitter', 'https://twitter.com/feigaochn'),
    ('weibo', 'http://weibo.com/feigaochn'),
    ('flickr', '#'),
    ('spotify', '#'),
)
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
# TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
# RECENT_POST_COUNT = 5

# Disqus comments
# DISQUS_NO_ID = False
DISQUS_DISPLAY_COUNTS = False

# Content license
CC_LICENSE = "CC-BY"

# twitter cards
TWITTER_CARDS = True

# twitter timeline
TWITTER_USERNAME = 'feigaochn'
TWITTER_WIDGET_ID = '558567974076829696'

# AddThis
# ADDTHIS_PROFILE = 'profile_id'
