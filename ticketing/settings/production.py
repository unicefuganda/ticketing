import os

from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "public", "static")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ticketing',
        'USER': 'ticketing',
        'PASSWORD':'',
        'HOST': 'dbserver',
        'PORT': 6543,
    }
}
