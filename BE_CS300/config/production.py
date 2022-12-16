from BE_CS300.settings import *

import os

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', "").split(',')

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USERNAME'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

DEBUG = True

AWS_S3_ENDPOINT_URL = None

CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', "").split(',')

STATIC_URL = f'/{STATIC_LOCATION}/'
MEDIA_URL = f'/{PUBLIC_MEDIA_LOCATION}/'
