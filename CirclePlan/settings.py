"""
Django settings for CirclePlan project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')-+7_g8%h3%epsr!aka#^wqphp-5bx047%yi5zg6^ivfmah=)2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'django.db.models',
    'admin_reorder',
    'psycopg2_extension',
    'rest_framework',
    'corsheaders',
    'clear_cache',
    'crispy_forms',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'instructors.apps.InstructorsConfig',
    'yashuvim.apps.YashuvimConfig',
    'attendance.apps.AttendanceConfig',
    


]



CRISPY_TEMPLATE_PACK =  'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'CirclePlan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR),'templates'],
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
WSGI_APPLICATION = 'CirclePlan.wsgi.application'
CSRF_COOKIE_SECURE = True
LOGOUT_REDIRECT_URL = 'index'

ADMIN_TOOLS_MENU = 'CirclePlan.menu.CustomMenu'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CirclePlan',
        'USER': 'postgres',
        'PASSWORD': '1a2a3a4a',
        'HOST' : 'localhost'

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'CirclePlan/static')
]

# corsheaders
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'https://attendency-web.herokuapp.com',
]

# rest_framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
}


# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

ADMIN_REORDER = (


    # Reorder app models




    {'app': 'auth', 'models': ('auth.User', 'auth.Group')},
    {'app': 'attendance', 'models' : ('attendance.Member', 'attendance.Meeting','attendance.Participation',) },
    {'app': 'attendance', 'models' : ('attendance.Circle', ),'label': 'Circles'},
    {'app': 'yashuvim' },




)

# {'app': 'attendance', 'models':('attendance.Meetings', 'attendance.Members','attendance.Participations')},
#Circles




"""
#Email config
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
"""
