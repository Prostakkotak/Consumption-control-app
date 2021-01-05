import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3(mytum)rh8$ttgx6p4x76w&g)6f_3^5wi#4g_4vku_rxeeqlo'

DEBUG = True

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'std_1388',
        'USER': 'std_1388',
        'PASSWORD': 'vaskovsky',
        'HOST': 'std-mysql.ist.mospolytech.ru',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (STATIC_DIR,)