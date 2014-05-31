#!/bin/bash

source ~/dev.pycon.kr/bin/activate
rm -rf ./collected_static/
pip install -r requirements.pip
./manage.py flush --noinput --settings=settings.deploy
./manage.py syncdb --noinput --settings=settings.deploy
./manage.py collectstatic --noinput --settings=settings.deploy
kill -HUP `cat /home/deploy/pyconkr.pid`
# service reload?


cp /home/svc/pyconkr/conf/nginx.conf /etc/nginx/sites-available/pyconkr.conf
ln -sf /etc/nginx/sites-available/pyconkr.conf /etc/nginx/sites-enabled/pyconkr.conf
cp /home/svc/pyconkr/conf/uwsgi.ini /etc/uwsgi/apps-available/pyconkr.ini
ln -sf /etc/uwsgi/apps-available/pyconkr.ini /etc/uwsgi/apps-enabled/pyconkr.ini
service nginx $1
/home/svc/envs/pyconkr/bin/python manage.py collectstatic --noinput
service uwsgi $1