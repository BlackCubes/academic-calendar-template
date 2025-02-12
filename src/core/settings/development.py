# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-p=%1sijcyd)gwm6&bn8il^t%3y6abn71jh#ea4@pji#onsxm-+"

ALLOWED_HOSTS = [""]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
]
