import os

from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "public", "static")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ticketing',
        'USER': 'ticketing',
        'PASSWORD': '',
        'HOST': 'dbserver',
        'PORT': 6543,
    }
}

HELPDESK_VIEW_A_TICKET_PUBLIC = True
HELPDESK_SUBMIT_A_TICKET_PUBLIC = False
HELPDESK_DASHBOARD_BASIC_TICKET_STATS = True
HELPDESK_FOOTER_SHOW_CHANGE_LANGUAGE_LINK = True
HELPDESK_FOOTER_SHOW_API_LINK = True

RAVEN_CONFIG = {
    'dsn': 'http://496b2d50a2a8469294929e7775d56ea5:'
           '0528086b2cb64e1a964973e5b2d80450@sentry.unicefuganda.org/5',
}
