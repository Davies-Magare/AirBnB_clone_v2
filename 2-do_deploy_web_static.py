#!/usr/bin/python3
from fabric.api import env, run, local, put
from datetime import datetime
import os
"""
Compress webstatic directory into a tar file with Fabric.
"""

env.hosts = ['ubuntu@35.174.208.95', 'ubuntu@100.26.174.14']
env.key_filename = '~/.ssh/school'


def do_pack():
    """Compress a webstatic directory into a tar file with Fabric."""
    try:
        local('mkdir -p versions 2>/dev/null')
        time = datetime.now()
        timestamp = time.strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(timestamp)
        local('tar -czvf {} web_static'.format(path))
        return path
    except Exception:
        return None


def do_deploy(archive_path):
    """Transfer file to remote host and decompress it."""

    if not os.path.exists(archive_path):
        return False

    for host in env.hosts:
        try:
            # Transfer archive to remote server
            put(local_path=archive_path, remote_path='/tmp/')
            # Extract archive to the correct directory
            filename = os.path.basename(archive_path).split('.')[0]
            extract_path = "/data/web_static/releases/{}".format(filename)
            original_path = "/tmp/{}.tgz".format(filename)
            run("mkdir -p {}".format(extract_path))
            run("tar -xvzf {} -C {}".format(original_path, extract_path))
            # Clean up the temporary archive on the remote server
            run("rm -f /tmp/{}.tgz".format(filename))
            sym_link = '/data/web_static/current'
            run("rm -f {}".format(sym_link))
            run("ln -s {} {}".format(extract_path, sym_link))
            return True
        except Exception as e:
            return False
