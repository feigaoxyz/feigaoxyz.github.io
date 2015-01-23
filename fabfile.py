#encoding=utf-8
from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf cache')
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    rebuild()
    serve()

def preview():
    local('pelican -s publishconf.py')

def repreview():
    rebuild()
    preview()

# def cf_upload():
    # rebuild()
    # local('cd {deploy_path} && '
          # 'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          # '-U {cloudfiles_username} '
          # '-K {cloudfiles_api_key} '
          # 'upload -c {cloudfiles_container} .'.format(**env))

# @hosts(production)
# def publish():
    # local('pelican -s publishconf.py')
    # project.rsync_project(
        # remote_dir=dest_path,
        # exclude=".DS_Store",
        # local_dir=DEPLOY_PATH.rstrip('/') + '/',
        # delete=True,
        # extra_opts='-c',
    # )


def github(publish_drafts=False):
    preview()
    try:
        if os.path.exists('output/drafts'):
            if not publish_drafts:
                local('rm -rf output/drafts')
    except Exception:
        pass
    local('ghp-import -m "Generate Pelican site" -b master output')
    local('git push origin master')

from datetime import datetime

TEMPLATE = u"""
Title: {title}
Date: {year}-{month:02d}-{day:02d}
Slug: {slug}
Tags:
Summary:
Status: draft

"""
def make_entry(title):
    title = title.decode('utf-8')
    # print(type(title))
    import pypinyin
    import jieba
    today = datetime.today()
    # slug = title.lower().strip().replace(' ', '-')
    slug = pypinyin.slug(title, errors='ignore').lower()
    f_create = "content/drafts/{}-{:0>2}-{:0>2}_{}.md".format(
        today.year, today.month, today.day, title.encode('utf-8'))
    t = TEMPLATE.lstrip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                slug=slug.encode())
    print(type(t))
    with open(f_create, 'a') as w:
        w.write(t.encode('utf-8'))
    print("File created -> " + f_create)
    print(t)
