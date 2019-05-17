"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c3le&g_61hr@^@d7v*q6sbwd9)84ssdthcgi8pw^@w!7e!v5l+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','146.232.93.23','146.232.66.100','146.232.66.118']


# Application definition

INSTALLED_APPS = [
    'myapp.apps.MyappConfig', # format for renaming django apps
    'calendarevents.apps.CalendareventsConfig',
    #'grappelli',#install grappelli first (silenced skinns)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'archivesuploads.apps.ArchivesuploadsConfig', # format for renaming django apps
    'News',
   #'contactus',
   'djgeojson', # application for maps in django on django admin # pip3 install "django-geojson [field]"
   'leaflet', # application for maps in django on django admin
   'contactus.apps.ContactusConfig',
  # 'passwordmanager', # sacema password manager application
   'passwordmanager.apps.PasswordmanagerConfig', #format for renaming django apps
    #'contactus.apps.ContactusConfig', # format for renaming django apps
    #'myapp',#add new app
    #'archivesuploads',
    'import_export', #pip3 install openpyxl==2.4.9, pip3 install django-import-export
    #'people_manager.apps.People_managerConfig',
    #'People_Manager',#Student staff MIS
    #'peoplemanager',# student staff MIS
    'peoplemanager.apps.PeoplemanagerConfig',
    'TRAP', # Tsetse application
    #'admin_reorder', #  for reordering apps #pip install django-modeladmin-reorder
    #'constrainedfilefield', #pip install django-constrainedfilefield[filetype]
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases connection string

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # pip3 install mysqlclient
        'NAME': 'sacema02',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False # changed to false from True so as to pick the current time zo


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/



STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_DIRS = 'static'
#STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = '/media/' #media root configuration
MEDIA_ROOT = os.path.join(BASE_DIR,"media") #media root configuration





CONTENT_TYPES = ['file']
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "5242880"
