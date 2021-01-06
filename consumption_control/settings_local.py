import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '3(mytum)rh8$ttgx6p4x76w&g)6f_3^5wi#4g_4vku_rxeeqlo'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('db.sqlite3'),
=======
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'std_1388',
        'USER': 'std_1388',
        'PASSWORD': 'vaskovsky',
        'HOST': 'std-mysql.ist.mospolytech.ru',
        'PORT': '3306',
>>>>>>> 0552e4f6c5d0b2ce4fb2bd5c2a2670f55c7a9c2c
    }
}

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (STATIC_DIR,)