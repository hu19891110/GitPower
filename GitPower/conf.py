# encoding: utf-8
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gitp',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '21345',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.getcwd() + '/Media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://42.120.17.216/'

GIT_HOOKS_DIR = "%s/.gitpower/hooks"%os.getenv("HOME")

DATE_INPUT_FORMAT = '%Y-%m-%d'

#the app visit url
APP_URL="http://localhost:8000/assets"

#the app domain
APP_DOMAIN = "gitpower.com"

#the gitlote bin path default is {home}/.gitlite
GITLOTE_PATH = "%s/.gitolite"%os.getenv("HOME")

#git repositories path default is {home}/repositories
REPOS_PATH = "%s/repositories"%os.getenv("HOME")

#git bin path
GIT_PATH = "/usr/bin/git"


DEFAULT_FILE_STORAGE = 'Common.store.YPStorage'

STORE_BUCKET = ''

STORE_USER  = ''

STORE_PASSWORD = ''

EMAIL_USE_TLS = False
EMAIL_HOST = 'SMTP HOST'
EMAIL_HOST_USER = 'SMTP USER'
EMAIL_HOST_PASSWORD = 'SMTP PASSWORD'
EMAIL_PORT = 25

SITE_PUBLIC = True