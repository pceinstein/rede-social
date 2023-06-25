"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l*1jtc8&s$_+b#r-*uf+#ti39*6sxdg19%0&w%-8=_^)^&7ha!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django_extensions',
    'images.apps.ImagesConfig',
    'easy_thumbnails',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmarks.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Login urls
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# configuração para o Django escrever emails no console, para teste
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Permitir que o servidor Django sirva os arquivos de mídia carregados pelo usuário
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# backends de autenticação
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',    # default
    'account.authentication.EmailAuthBackend',      # personalizado
    'social_core.backends.facebook.FacebookOAuth2', # autenticação com o Facebook
    'social_core.backends.twitter.TwitterOAuth',    # autenticação com o Twitter
    'social_core.backends.google.GoogleOAuth2',     # autenticação com o Google
]


# Configurações para log-in com redes sociais
SOCIAL_AUTH_FACEBOOK_KEY = os.environ['SOCIAL_Facebook_Key']        # ID do App Bookmarks no Facebook
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['SOCIAL_Facebook_Secret']  # Senha do App Bookmarks no Facebook
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']  # Permissões extras para solicitar aos usuários do Facebook

SOCIAL_AUTH_TWITTER_KEY = os.environ['SOCIAL_Twitter_Key']          # ID do App Bookmarks no Twitter
SOCIAL_AUTH_TWITTER_SECRET = os.environ['SOCIAL_Twitter_Secret']    # Senha do App Bookmarks no Twitter

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['SOCIAL_Google_Key']         # ID do App Bookmarks no Google
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['SOCIAL_Google_Secret']   # Senha do App Bookmarks no Google


# Especificar o URL para um modelo
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}