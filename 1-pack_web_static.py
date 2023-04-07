#!/usr/bin/python3
'''script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder'''

    local("mkdir -p versions")   # create the directory if it doesnt exist
    arch_name = "web_static_{}".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local('tar -czvf versions/{}.tgz web_static'.format(arch_name))
    if result.succeeded:
        return "versions/{}.tgz".format(arch_name)
    else:
        return None
