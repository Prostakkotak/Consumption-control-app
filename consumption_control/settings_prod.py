import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '3(mudkg)rh8$gjrudijth76w&g)6f_3^5wi#4g_ulaik_rxeeqlo'

DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ["consumption-control.std-1388.ist.mospolytech.ru"]
=======
ALLOWED_HOSTS = ["127.0.0.1", "std-1388.ist.mospolytech.ru", "172.16.120.10"]
>>>>>>> 0552e4f6c5d0b2ce4fb2bd5c2a2670f55c7a9c2c

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


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_DIR = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = (STATIC_DIR,)