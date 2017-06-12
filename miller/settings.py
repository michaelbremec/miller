#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for miller project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os, sys
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

management_command = sys.argv[1] if len(sys.argv) > 1 else ""
TESTING = management_command.startswith("test")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'change in your localsettings'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

APPEND_SLASH = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.postgres.search',
    'social.apps.django_app.default',
    'channels',
    'oauth2_provider',
    'rest_framework',
    'templated_email',
    'djoser',
    'ws4redis',
    'simplemde',
    'captcha',
    'miller',
    'actstream',
    'dbbackup'
    #'django_seo_js'
    
]

DBBACKUP_STORAGE         = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, 'backup')}
DBBACKUP_DATE_FORMAT     = '%Y-%m-%d'

MIDDLEWARE_CLASSES = [
    #'django_seo_js.middleware.UserAgentMiddleware',  # If you want to detect by user agent
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'miller.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'client')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'social.apps.django_app.context_processors.backends',
#                 'social.apps.django_app.context_processors.login_redirect',
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 # 'django.core.context_processors.static',
#                 'ws4redis.context_processors.default',
#                 'miller.context_processors.default',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'miller.wsgi.application'

# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'client/src'),
# ]

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME':  os.path.join(BASE_DIR, 'test.db.sqlite3'),
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization. Restrict the list of availble language for the website.
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# THe forth element in each tuple item is the indexing language to be used with to_vector in portgresql.
# cfr. https://docs.djangoproject.com/en/dev/ref/contrib/postgres/search/
# since it dinamically adds language-related search fields to models
LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('fr-fr', _('French'), 'fr_FR', 'french'),
    ('de-de', _('German'), 'de_DE', 'german'),
    ('en-us', _('US English'), 'en_US', 'english'),
    # ('en-gb', _('British English'), 'en_GB', 'english'),
]


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'PAGE_SIZE': 4
}

SIMPLEMDE_OPTIONS = {
    'autosave': {
        'enabled': True
    },
    
    'spellChecker': False
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'dist')
MEDIA_URL   = '/media/'
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
ZIP_ROOT    = os.path.join(MEDIA_ROOT, 'zip')
    
# media files will be stored here as technical copies. It has to be related to MEDIA root
MEDIA_PRIVATE_RELATIVE_PATH  = 'private'
MEDIA_PRIVATE_ROOT = os.path.join(MEDIA_ROOT, 'private')


GIT_ROOT = os.path.join(BASE_DIR, 'contents')
GIT_COMMITTER = {
    'name': "A committer", 
    'email': "committer@example.com"
}

PROFILE_PATH_ROOT = os.path.join(GIT_ROOT, 'users')
REVIEWS_PATH_ROOT = os.path.join(GIT_ROOT, 'reviews')

#............
#
# MILLER STATIC MARKDOWN PAGES
# cfr. miller.context_processors.default
#............
PAGES_ROOT = os.path.join(BASE_DIR, 'client/src/pages')


SITE_ID=1

#............
#
# SOCIAL AUTH
#
#............
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_USER_MODEL = 'auth.User'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'email']
SOCIAL_AUTH_UUID_LENGTH = 16
# override these settings in your local_settings.py file, cfr. http://psa.matiasaguirre.net/docs/configuration/settings.html
AUTHENTICATION_BACKENDS = (
  #'social.backends.google.GoogleOAuth2',
  # 'social.backends.twitter.TwitterOAuth',
  'django.contrib.auth.backends.ModelBackend',
)

#............
#
# WHOOSH
#
#............
WHOOSH_ROOT = os.path.join(BASE_DIR, 'whoosh')

#............
#
# RSS
#
#............
RSS_TITLE = 'Miller'
RSS_DESCRIPTION = 'Miller description'

#............
#
# REDIS
#
#............
WEBSOCKET_URL = '/ws/'
WS4REDIS_EXPIRE = 7200
WS4REDIS_PREFIX = 'miller'

#............
#
# django-redis-session
# https://github.com/martinrusev/django-redis-sessions
#............
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_DB = 3
# If the Redis datastore uses connection settings other than the defaults, use this dictionary to override these values
# WS4REDIS_CONNECTION = {
#     'host': 'localhost',
#     'port': 16379,
#     'db': 17,
#     'password': 'verysecret', # override these settings in your local_settings.py file
# }

#............
#
# ACTSTREAM
# http://django-activity-stream.readthedocs.io/en/latest/data.html
#............
ACTSTREAM_SETTINGS ={
  'USE_JSONFIELD': True
}

#............
#
# LOGGING
#
#............
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'debug.log'),
            'formatter': 'lite'
        },
        'commands': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'commands.log'),
            'formatter': 'lite'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'lite':{
            'format': '%(levelname)s - %(asctime)s - %(module)s:%(lineno)s - %(funcName)20s - %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'miller.commands': {
            'handlers': ['commands'],
            'level': 'DEBUG'
        },
        'console': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'miller': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#............
#
# Django channels
#
#............

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "ROUTING": "miller.routing.channel_routing",
    },
}

#............
#
# CODEMIRROR PLUGIN ADMIN
#
#............

CODEMIRROR_PATH = r'js/codemirror'


#............
#
# DJANGO-REGISTRATION SETTINGS
# 
#............
ACCOUNT_ACTIVATION_DAYS = 7


#............
#
# DJANGO-REDIS-CACHE
# 
#............
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {
            'DB': 2,
        }
    },
}

#............
#
# MILLER APP
#
#............
MILLER_WS_HOST = None # override in your localsettings with the full address for your websocket e;g. ws://resume.cvce.eu
MILLER_HOST_PROTOCOL = 'http' # used by miller.sitemaps module
MILLER_DEBUG = True

MILLER_TITLE = 'Miller'
MILLER_DESCRIPTION = 'Developed by the University of Luxembourg'
MILLER_SIGNEDBY = u'Miller Editorial Team\n'

MILLER_LOCALE = os.path.join(BASE_DIR, 'client/src/locale/locale-all.csv')
MILLER_LOCALE_ROOT = os.path.join(BASE_DIR, 'client/src/locale')

MILLER_LOCALISATION_TABLE = os.path.join(BASE_DIR, 'client/src/locale/locale-all.csv')

MILLER_TEX = os.path.join(BASE_DIR, 'miller.tex')

# default width value for helpers generate_snapshot. Set width OR height to None or to 0 means following the original image ratio.
MILLER_SNAPSHOT_WIDTH = 234
MILLER_SNAPSHOT_HEIGHT = None


# feel free to add your own oembed service in localsettings.
MILLER_OEMBEDS = {
  'vimeo':  {
    'endpoint': 'https://vimeo.com/api/oembed.json'
  }
}

CSRF_COOKIE_NAME = 'Miller'

MILLER_SETTINGS = {
  'wshost': MILLER_WS_HOST,
  'host': 'http://', #check your local_settings.py file
  'debug': MILLER_DEBUG,
  'disqus': '',
  'socialtags': 'resume-unilu', # socila tags when sharing on twitter
  'analytics': 'UA-XXXXXXX-1',
  'copyright': '',
  'copyrighturl': '',
}

# in seconds
MILLER_URL_REQUEST_TIMEOUT = 15

# please check that in your static pages root there are .md files for each of these pagenames
MILLER_STATIC_PAGES = ['guide-for-authors', 'people', 'project', 'terms-of-use']
MILLER_STATIC_PAGES_ROOT = os.path.join(BASE_DIR, 'client/src/pages')

# the settings above are the generic ones. Shall you need to change something, override the default values in a local_settings.py file instead.
try:
    from local_settings import *
except ImportError:
    pass
