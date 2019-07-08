"""
Django settings for django_test project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs/.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')so+a!bo41g+jwvw0searr)ne_!1og8q*dld*a40!=27z7r&lw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'django_filters',
    'corsheaders',
    'rest_framework.authtoken',
    'sys_user',
    'DemoApp',
    'SceneApp',
    'AccessApp',
    'DeviceApp',
    'log',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',# add用来解决跨域
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'django_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'django_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        #'HOST':'111.230.200.183',
        'PORT':'3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'zh-hans' #语言配置

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES':(

'rest_framework.parsers.JSONParser',
          'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    # 'GLOBAL_CSRF_CHECK':False
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        )
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS':
 {
        'basic': {
            'type': 'basic'
        }
    },
    'JSON_EDITOR' : False,
    'LOGIN_URL' : 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'SHOW_REQUEST_HEADERS':True,
    'VALIDATOR_URL':None,
}

import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA':datetime.timedelta(days=1),
    'JWT_AUTH_HEADER_PREFIX':'JWT',
    #'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler',
 }


CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = ( '*' )
CORS_ALLOW_METHODS = ('DELETE', 'GET', 'OPTIONS','PATCH','POST','PUT','VIEW', )
CORS_ALLOW_HEADERS = ('XMLHttpRequest','X_FILENAME','accept-encoding','authorization','content-type','dnt','origin','user-agent','x-csrftoken','x-requested-with','Pragma', )



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')