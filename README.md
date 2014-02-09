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
수행시에 다음과 같이 한다. ( db sync 작업 및 서버 구동 )
```
python manage.py syncdb --settings=settings.py
python manage.py runserver --settings=settings.py
```

세팅 파일 변경하여 실행하는 방법
-------------------------

    ex)
    python manage.py runserver --settings=settings.local
    python manage.py runserver --settings=settings.deploy
    python manage.py runserver --settings=settings.py

