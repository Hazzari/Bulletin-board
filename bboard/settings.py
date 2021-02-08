import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()  # reading .env file
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
DATABASES = {'default': env.db()}

# Email
if DEBUG:
    EMAIL_PORT = 1025

else:
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS')

if DEBUG:
    # Псевдо кэш для отладки
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
else:
    # Redis
    CACHES = {
        'default': env.cache('REDIS_URL'),
    }

# Application definition
INSTALLED_APPS = [
    # Django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'bootstrap4',
    'django_cleanup',
    'easy_thumbnails',
    'captcha',

    # Created apps
    'main.apps.MainConfig',
    'api.apps.ApiConfig'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGINAL_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

ROOT_URLCONF = 'bboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.middlewares.bboard_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'bboard.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]
AUTH_USER_MODEL = 'main.AdvUser'

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.parent / 'static'
MEDIA_ROOT = BASE_DIR.parent / 'media'
MEDIA_URL = '/media/'

THUMBNAIL_ALIASES = {'': {'default': {'size': (96, 96), 'crop': 'scale'}, }, }
THUMBNAIL_BASEDIR = 'thumbnails'
