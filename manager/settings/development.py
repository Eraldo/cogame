__author__ = 'eraldo'

from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'manager/fixtures/'),
)