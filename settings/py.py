# coding=utf-8
# 여기는 py만 쓰는 공간입니다. 이런식으로 각자 개발자들이 필요한 세팅파일 직접 만들어서 쓰세요.
from pyconkr.settings import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'pyconkr.sqlite3'),
    }
}
