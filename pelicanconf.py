#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marta Alonso'
SITENAME = u'Inicio'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'es'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = (('El diario de Passepartout', 'http://eldiariodepassepartout.blogspot.com/'),
         ('Molaviajar', 'http://www.molaviajar.com//'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/marta_alonso_f'),
          # ('linkedin', 'https://es.linkedin.com/pub/juan-elosua/b/274/689'),
          # ('github', 'https://github.com/malon'),)
			)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#Markdown extensions
MD_EXTENSIONS = ['extra']

#THEME
#THEME = 'html5-dopetrope'
#THEME = 'pelican-blueidea'
#THEME = 'alchemy'
#THEME = 'pelican-fresh'
#THEME = 'plumage'
THEME = 'nest'
#THEME = 'notmyidea'

NEST_HEADER_IMAGES = 'gardel.resized.JPG'
# SITESUBTITLE = u'My Awesome Blog'
#MENUITEMS = [('Homepage', '/'),('Categories','/categories.html')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_LOGO = '/images/logo3.resized.png'

# index.html
NEST_INDEX_HEAD_TITLE = u'Boludeces a la gallega'
NEST_INDEX_HEADER_TITLE = u'Boludeces a la gallega'
NEST_INDEX_HEADER_SUBTITLE = u'Aventuras y ocurrencias de dos emigrantes modernos en la Argentina'
NEST_INDEX_CONTENT_TITLE = u'Boludeces varias:'


# Add items to top menu before pages
MENUITEMS = [('Categorías','/categories.html'),('Etiquetas','/tags.html')]
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archivo'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Archivo de entradas'
NEST_ARCHIVES_HEADER_TITLE = u'Archivo'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archivo de todas las entradas'
NEST_ARCHIVES_CONTENT_TITLE = u'Archivo'
# # article.html
NEST_ARTICLE_HEADER_BY = u'Por'
NEST_ARTICLE_HEADER_MODIFIED = u'modificado'
NEST_ARTICLE_HEADER_IN = u'en categoría'
# author.html
# NEST_AUTHOR_HEAD_TITLE = u'Posts by'
# NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
# NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
# NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
# NEST_AUTHORS_HEAD_TITLE = u'Author list'
# NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
# NEST_AUTHORS_HEADER_TITLE = u'Author list'
# NEST_AUTHORS_HEADER_SUBTITLE = u'Archives listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categorías'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archivos listados por categoría'
NEST_CATEGORIES_HEADER_TITLE = u'Categorías'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archivos listados por categoría'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Archivo de categoría'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Archivo de categoría'
NEST_CATEGORY_HEADER_TITLE = u'Categoría'
NEST_CATEGORY_HEADER_SUBTITLE = u'Archivo de categoría'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Archivo de etiqueta'
NEST_TAG_HEAD_DESCRIPTION = u'Archivo de etiqueta'
NEST_TAG_HEADER_TITLE = u'Etiqueta'
NEST_TAG_HEADER_SUBTITLE = u'Archivo de etiqueta'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Etiquetas'
NEST_TAGS_HEAD_DESCRIPTION = u'Lista de etiquetas'
NEST_TAGS_HEADER_TITLE = u'Etiquetas'
NEST_TAGS_HEADER_SUBTITLE = u'Lista de etiquetas'
NEST_TAGS_CONTENT_TITLE = u'Lista de etiquetas'
NEST_TAGS_CONTENT_LIST = u'etiquetado'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Mapa'
# NEST_SITEMAP_MENU = [('Archivo', '/archives.html'),('Authors','/authors.html')]
NEST_SITEMAP_MENU = [('Archivo', '/archives.html'),('Etiquetas','/tags.html'),('Categorías','/categories.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Otros Blogs'
#NEST_COPYRIGHT = u'&copy; Las Boludeces de Gallega 2015'

# Static files
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
   # 'extra/robots.txt': {'path': 'robots.txt'},
    # 'extra/favicon.ico': {'path': 'favicon.ico'},
    # 'extra/logo.svg': {'path': 'logo.svg'},
    'extra/.gitignore_prod': {'path': '.gitignore'}
}