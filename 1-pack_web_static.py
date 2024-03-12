#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
"""Compress webstatic directory into a tar file with Fabric."""

def do_pack():
    try:
        local('mkdir -p versions 2>/dev/null')
        time = datetime.now()
        timestamp = time.strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(timestamp)
        local('tar -czvf {} web_static'.format(path))
        return path
    except Exception:
        return None
