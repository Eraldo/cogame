"""Development settings and globals."""


from .base import *

__author__ = 'eraldo'


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# DATABASES = {}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
    'sslserver',
)
#
# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )
#
# DEBUG_TOOLBAR_PATCH_SETTINGS = False
#
# # http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
# INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION


########## BOOTSTRAP3 CONFIGURATION
BOOTSTRAP3.update(
    {
        'jquery_url': '{}website/bower_components/jquery/dist/jquery.min.js'.format(STATIC_URL),
        'base_url': '{}website/bower_components/bootstrap/dist/'.format(STATIC_URL),
    }
)
########## END BOOTSTRAP3 CONFIGURATION