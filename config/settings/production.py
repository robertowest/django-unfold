from .base import *

DEBUG = False

SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = [
    'https://lookingfor.es',
    'https://www.lookingfor.es',
]

