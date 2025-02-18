"""
Django settings for Pagina project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path
import cloudinary # type: ignore
import cloudinary.uploader # type: ignore
import cloudinary.api # type: ignore

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qftm167prsk3re)s@7sxov994^fsyy8sx-3x+u1+tu!4@0q58@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'admin_confirm',
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'crispy_forms',
    'crispy_bootstrap4',
    'rest_framework',
    'axes',
    'captcha',
    'django_recaptcha',
    'cloudinary',
]

# Config Multi-Captcha
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

X_FRAME_OPTIONS = "SAMEORIGIN"
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'Pagina.urls'

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

WSGI_APPLICATION = 'Pagina.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'aws-0-sa-east-1.pooler.supabase.com',
        'NAME': 'postgres',
        'USER': 'postgres.vodlhrgxryneuvekuedi',
        'PASSWORD': 'MechanicMayhem2024',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

RECAPTCHA_PUBLIC_KEY = '6LeiLfcpAAAAAJVyoycei3bDHfP10j3V3qSzTpM7'
RECAPTCHA_PRIVATE_KEY = '6LeiLfcpAAAAAFk-SR4DVjYtZ4C7LkrSX59z5ZVy'

AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

AXES_FAILURE_LIMIT = 3 #Intentos fallidos por usuario
AXES_COOLOFF_TIME = timedelta(minutes=5) #Cantidad de tiempo antes de intentar Login
AXES_LOCKOUT_URL = '/account_locked/'
AXES_RESET_ON_SUCCES = True #Resetea contador de fallos cuando hay Login exitoso

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#python manage.py collectstatic --upload-unhashed-files

#CONFIG CLOUDINARY
cloudinary.config(
    cloud_name='dapibed5f',
    api_key='692897366215152',
    api_secret='td6YHUa51DJ7E7RFiKBG9QK0rLs'
)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

#Configuraciones para msj
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

#CONFIGURACIONES LOGIN Y LOGOUT
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#CONFIGURACIÓN DE EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "mechanic.mayhem.chile@gmail.com"
EMAIL_HOST_PASSWORD = "MechanicMayhem2024Ayuda"   

#CONFI PARA GUARDAR LAS IMG
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


