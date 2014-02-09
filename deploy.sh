#!/bin/bash

source ~/dev.pycon.kr/bin/activate
pip install -r requirements.pip
pip install mysql-python
./manage.py flush --settings=settings.deploy
./manage.py collectstatic --noinput --settings=settings.deploy
# service reload?
