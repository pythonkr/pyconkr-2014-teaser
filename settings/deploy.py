# coding=utf-8
# 여기에 배포용 세팅을 쓰시면 됩니다. 되도록 환경변수를 활용하면 좋겠네요.
from pyconkr.settings import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
