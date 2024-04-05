#!/usr/bin/python3
"""Create a tar archive locally using fabric."""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Create a tar archive using fabric."""
    try:
        local('mkdir versions')
        now = datetime.now()
        time_string = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(time_string)
        local("tar -czvf versions/{} -C web_static .".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None
