PyConKr
=======

설치
---
### Mac os x
맥은 이미 파이썬이 설치되어 있으므로,
```sh
easy_install pip
sudo pip install -r requirements.pip
```

세팅 파일 변경하여 실행하는 방법
-------------------------

    ex)
    python manage.py runserver --settings=settings.local
    python manage.py runserver --settings=settings.deploy
    python manage.py runserver --settings=settings.py

