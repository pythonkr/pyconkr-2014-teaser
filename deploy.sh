#!/bin/bash

source ~/dev.pycon.kr/bin/activate
rm -rf ./collected_static/
pip install -r requirements.pip
pip install mysql-python
./manage.py flush --noinput --settings=settings.deploy
./manage.py syncdb --noinput --settings=settings.deploy
./manage.py collectstatic --noinput --settings=settings.deploy
kill -HUP `cat /home/deploy/pyconkr.pid`
# service reload?
