# -*- coding: utf-8 -*-
from fabric.api import local, run, cd, env, prefix

env.hosts = ['dev.pycon.kr']
env.user = 'deploy'
env.target = 'dev'
env.virt_activate = '. ~/venv.dev.pyconkr/bin/activate'
env.apps_dir = '~/dev.pyconkr'

def prod():
    env.virt_activate = '. ~/venv.www.pyconkr/bin/activate'
    env.apps_dir = '~/www.pyconkr'

def dev():
    pass

def server_init():
    # ubuntu server only
    with prefix('sudo'):
        run('apt-get update')
        run('apt-get install nginx')
        run('apt-get install uwsgi')
        run('apt-get install build-essential python-pip python-dev libjpeg-dev libfreetype6-dev zlib1g-dev')
        run('pip install virtualenv')
    run('git clone git@github.com:pythonkr/pyconkr.git')
    run('mkvirtualenv venv.pyconkr')
    with prefix('sudo'):
        run('cp ~/pyconkr/settings/nginx/pycon.kr /etc/nginx/sites-available/')
        run('ln -s /etc/nginx/sites-available/pycon.kr /etc/nginx/sites-enabled/')
        run('cp ~/pyconkr/settings/uwsgi/pyconkr.ini /etc/uwsgi/apps-available/')
        run('ln -s /etc/uwsgi/apps-available/pyconkr.ini /etc/uwsgi/apps-enabled/')
        run('/etc/init.d/nginx restart')
        run('/etc/init.d/uwsgi restart')


def deploy(commit_id=None):
    rev = local('git rev-parse HEAD', capture=True)
    if commit_id:
        rev = str(commit_id)
    
    with prefix(env.virt_activate):
        with cd(env.apps_dir):
            run('git fetch -p')
            run('git reset --hard %s' % rev)
            run('pip install -r requirements.pip')
            run('python manage.py collectstatic --noinput')
            run('python manage.py compress')
            run('python manage.py migrate')
            run('find . -name "*.pyc" -delete')
            run('sudo /etc/init.d/uwsgi reload')
