MILLER_TITLE = 'MILLER'
MILLER_DEBUG = False

SECRET_KEY = 'YOUR SUPER SECRET KEY'


AUTHENTICATION_BACKENDS = (
  # 'social.backends.google.GoogleOAuth2',
  # 'social.backends.twitter.TwitterOAuth',
  'django.contrib.auth.backends.ModelBackend',
)

# SOCIAL_AUTH_TWITTER_KEY = ''
# SOCIAL_AUTH_TWITTER_SECRET = ''


# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'XXXYYYZZ.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''



ZOTERO_API_KEY = 'XXX'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'USERNAME',
        'USER': 'DBNAME',
        'PASSWORD': 'PASSWORD'
    }
}

MILLER_OEMBEDS = {
  'EMBEDLY_API_KEY': 'xxx'
}

STATIC_ROOT = '/var/www/miller/dist'

MILLER_SETTINGS = {
  'debug': MILLER_DEBUG,
  'disqus': 'xxx'   
}