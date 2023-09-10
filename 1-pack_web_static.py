#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        if not os.path.exists("versions"):
            local('mkdir -p versions')
            t = datetime.now()
            f = "%Y%m%d%H%M%S"
            archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
            local('tar -cvzf {} web_static'.format(archive_path))
            return archive_path
    except:
        return None
