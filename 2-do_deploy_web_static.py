#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of
the web_static, using the function do_pack and that distributes
the archive to your web servers using do_deploy
'''

from fabric.api import local, run, put, get, env
from datetime import datetime
import os

env.hosts = ['3.86.13.6', '35.175.64.13']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    '''distributes an archive to your web servers
    '''
    if not os.path.exists(archive_path):  # check if path exists
        return False
    try:
        archive_name = archive_path.split('/')[-1]
        destination = "/data/web_static/releases/{}".format(archive_name[:-4])
        put(archive_path, '/tmp/')

        run('sudo mkdir -p {}'.format(destination))
        run('sudo tar -xvzf /tmp/{} -C {}'.format(archive_name, destination))
        run('sudo rm -r /tmp/{}'.format(archive_name))
        run('sudo mv {}/web_static/* {}'.format(destination, destination))
        run('sudo rm -rf {}/web_static'.format(destination))

        run('sudo rm /data/web_static/current')  # Delete link
        run('sudo ln -sf {} /data/web_static/current'.format(deatination))
        return True
    except Exception:
        return False
