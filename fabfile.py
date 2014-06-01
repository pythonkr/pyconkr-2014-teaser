# -*- coding: utf-8 -*-
from fabric.api import local, run, cd, env, prefix

env.hosts = ['dev.pycon.kr']
env.user = 'deploy'


def deploy(commit_id=None):
    rev = local('git rev-parse HEAD', capture=True)
    if commit_id:
        rev = str(commit_id)
    with prefix('. ~/venv.pyconkr/bin/activate'):
        with cd('~/pyconkr'):
            run('git fetch -p')
            run('git reset --hard %s' % rev)
            run('pip install -r requirements.pip')
            run('python manage.py collectstatic --noinput')
            run('python manage.py compress')
            run('find . -name "*.pyc" -delete')
            run('sudo /etc/init.d/uwsgi reload')