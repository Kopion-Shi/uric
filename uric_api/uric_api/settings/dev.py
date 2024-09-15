"""
Django settings for uric_api project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "root",
        "NAME": "uric",
    }
}

ALLOWED_HOSTS = ["127.0.0.1:8000","localhost","localhost:8080" ]

# CORS组的配置信息
CORS_ORIGIN_WHITELIST = (
    # 'www.uric.cn:8080', # 如果这样写不行的话，就加上协议(http://www.uric.cn:8080，因为不同的corsheaders版本可能有不同的要求)
    'http://127.0.0.1:8000',
)