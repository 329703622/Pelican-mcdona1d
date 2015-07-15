#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'mcdona1d'
SITENAME = u"mcdona1d's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('linkedin', 'https://cn.linkedin.com/pub/%E9%AA%9E-%E5%BC%A0/b4/172/432'),
          ('github', 'https://github.com/329703622'),
          ('weibo', 'http://weibo.com/234773130'),
          ('Instagram', 'https://instagram.com/q329703622/'),
          ('CSDN Blog', 'http://blog.csdn.net/u010027419'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#静态拷贝地址
STATIC_PATHS = ['images', 'static']

#静态拷贝文件
EXTRA_PATH_METADATA = {
    'images/favicon.png': {'path': 'favicon.png'},
    'images/avatar.jpg': {'path': 'avatar.jpg'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/CNAME': {'path': 'CNAME'},
    'static/张骞个人简历.pdf': {'path': '张骞个人简历.pdf'},
    'static/baidu_verify_RqEteSOLOU.html': {'path': 'baidu_verify_RqEteSOLOU.html'},
    'static/google7f1fe4ff07f6b848.html': {'path': 'google7f1fe4ff07f6b848.html'},
}
#忽略后缀名
READERS = {'html': None}
#使用目录名作为文章的分类名
USE_FOLDER_AS_CATEGORY = True

#使用文件名作为文章或页面的slug
FILENAME_METADATA = '(?P<slug>.*)'

#页面的显示路径和保存路径
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

#主题相关设置
FAVICON = 'images/favicon.png'
THEME='pelican-bootstrap3'
BOOTSTRAP_THEME='cerulean'

#顶横幅
#BOOTSTRAP_NAVBAR_INVERSE=True
BANNER = 'images/banner.jpg'
BANNER_SUBTITLE = 'Life is short live it up'
BANNER_ALL_PAGES = False
BOOTSTRAP_NAVBAR_INVERSE = False

MENUITEMS = (("Tags","http://mcdona1d.me/tags.html"),)

#右侧栏
AVATAR = 'avatar.jpg'
ABOUT_ME = """<h3 style="text-align:center">
<a href="http://weibo.com/234773130"                     target="_blank">
<i class="fa fa-weibo" style="text-align:center"></i></a>
<a href="https://github.com/329703622"                   target="_blank">
<i class="fa fa-github" style="text-align:center"></i></a>
<a href="https://www.facebook.com/mcdona1d"              target="_blank">
<i class="fa fa-facebook" style="text-align:center"></i></a>
<a href="https://twitter.com/329703622"                  target="_blank">
<i class="fa fa-twitter" style="text-align:center"></i></a>
<a href="https://plus.google.com/107873610420713613724/posts" target="_blank">
<i class="fa fa-google-plus" style="text-align:center"></i></a>
<a href="mailto:q329703622@hotmail.com" target="_blank">
<i class="mdi-communication-email" style="text-align:center"></i></a>
</h3>
"""

DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_TAGS_INLINE = True

GITHUB_SKIP_FORK=True
GITHUB_SHOW_USER_LINK=True
GITHUB_USER = '329703622'

#底栏
CC_LICENSE = "CC-BY-NC-SA"

#文章内设置
DISPLAY_ARTICLE_INFO_ON_INDEX=False

SHOW_ARTICLE_CATEGORY=True
SHOW_DATE_MODIFIED=True

PYGMENTS_STYLE = "monokai"
#Google +1
SHARIFF=True

#插件
PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = [
          'sitemap',
		      'tipue_search',
          'liquid_tags.img', 
          'liquid_tags.notebook',
          ]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

#DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search', 'tags')