#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of
the web_static, using the function do_pack and that distributes
the archive to your web servers using do_deploy
'''

from fabric.api import local, run, put, get, env
from datetime import datetime
import os

env.hosts = ['ubuntu@3.86.13.6', 'ubuntu@35.175.64.13']


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder'''

    local("mkdir -p versions")   # create the directory if it doesnt exist
    arch_name = "web_static_{}".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local('tar -czvf versions/{}.tgz web_static'.format(arch_name))
    if result.succeeded:
        return "/versions/{}".format(arch_name)
    else:
        return None


def do_deploy(archive_path):
    '''distributes an archive to your web servers
    '''
    if not os.path.exists(archive_path):  # check if path exists
        return False
    destination = "/data/web_static/releases/{}".format(archive_path[:-4])
    print("uploading archive")
    result = put(f'{archive_path}', '/tmp/{archive_path}')  # Upload the arch
    if result.failed:
        return False
    print("uncompressing archive")
    result = run(f'tar -xvzf /tmp/{archive_path} -C {destination}', hide=False, capture=True)
    if result.failed:
        return False
    print("deleting archive")
    result = run(f'sudo rm -r /tmp/{archive_path}')  # Delete the archive
    if result.failed:
        return False
    print("creating new symbolic link to latest version")
    result = run('sudo rm /data/web_static/current')  # Delete link
    if result.failed:
        return False
    result = run(f'ln -sf {destination} /data/web_static/current')
    if result.failed:
        return False
    return True
