# coding=utf-8
# 여기에 일반적인 개발환경의 로컬 세팅을 넣으시던지 하세요.
from pyconkr.settings import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
