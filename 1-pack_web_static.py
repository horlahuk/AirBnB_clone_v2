#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate an tgz archive from web_static folder"""
    dt = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}".format(dt.year,
                                                     dt.month,
                                                     dt.day,
                                                     dt.hour,
                                                     dt.minute,
                                                     dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
