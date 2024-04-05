#!/usr/bin/python3
"""Distribute archive to remote web servers."""


from fabric.api import env, put, run
import os

env.user = 'ubuntu'
env.key_filename = "/home/vagrant/.ssh/school"
env.hosts = ['34.224.62.243', '54.90.55.235']  # Define multiple hosts


def do_deploy(archive_path):
    """Distribute an archive to remote webservers."""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload file to web server
        put(archive_path, '/tmp/')
        run('ls /tmp/')
        # Decompress file
        filename = os.path.basename(archive_path)
        filename_no_extension = filename.split('.')[0]
        decompress_path = '/data/web_static/releases/{}'
        .format(filename_no_extension)
        run('mkdir -p {}'.format(decompress_path))
        upload_path = '/tmp/{}'.format(filename)
        run('tar -xzvf {} -C {}'.format(upload_path, decompress_path))
        # Delete archive from web server
        run('rm -f {}'.format(upload_path))
        # Delete symlink
        run('rm /data/web_static/current')
        # Create new symlink
        run('ln -s {} /data/web_static/current'.format(decompress_path))
        return True
    except Exception as e:
        print("Error occurred:", e)
        return False
