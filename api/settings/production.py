"""
Django settings for api project in development environment.

"""
from api.settings.settings import *
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
os.makedirs(STATIC_ROOT, exist_ok=True)
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEBUG_PROPAGATE_EXCEPTIONS = True
