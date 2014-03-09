#!/bin/bash

source ~/dev.pycon.kr/bin/activate

DJANGO_SETTINGS_MODULE=settings.deploy \
	/home/deploy/dev.pycon.kr/bin/gunicorn -b 127.0.0.1:9000 \
	--chdir /home/deploy/src \
	--max-requests 200 \
	-k gevent \
	-w 2 \
	-D \
	--pid /home/deploy/pyconkr.pid \
	pyconkr.wsgi:application
