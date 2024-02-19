import secrets
from .base import *


DEBUG = False
SECRET_KEY = secrets.token_urlsafe(37)
ADMINS = [
    ('Dylan Garrett', 'nullchamberdev@pm.me'),
]

ALLOWED_HOSTS = ['alphasite.com', 'www.alphasite.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432
    }
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
