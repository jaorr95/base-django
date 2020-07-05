"""
Django settings for api project in development environment.

"""
from api.settings.settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
	'USER': config('DATABASE_USER'),
	'PASSWORD': config('DATABASE_PASSWORD'),
	'HOST': config('DATABASE_HOST'),
	'PORT': config('DATABASE_PORT')
    }
}


