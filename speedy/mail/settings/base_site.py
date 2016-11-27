from speedy.net.settings.base import *

from .utils import APP_DIR

SITE_ID = int(env('SPEEDY_MAIL_SOFTWARE_SITE_ID'))

ROOT_URLCONF = 'speedy.mail.urls'

STATIC_ROOT = str(APP_DIR / 'static_serve')

TEMPLATES[0]['DIRS'].insert(0, str(APP_DIR / 'templates'))

LOCALE_PATHS.append(str(APP_DIR / 'locale'))

STATICFILES_DIRS.insert(0, str(APP_DIR / 'static'))

AUTH_SITE_PROFILE_MODEL = 'mail_accounts.SiteProfile'
