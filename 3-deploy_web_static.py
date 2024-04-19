#!/usr/bin/python3
"""Create and Distribute archive to remote web servers."""

from fabric.api import env, put, run
import os
import importlib

do_deploy = importlib.import_module('2-do_deploy_web_static').do_deploy
do_pack = importlib.import_module('1-pack_web_static').do_pack


def deploy():
    """Create and distribute the archive to webservers."""
    path = do_pack()
    if path is None:
        return False

    env.user = 'ubuntu'
    env.key_filename = "/home/vagrant/.ssh/school"
    env.hosts = ['34.224.62.243', '54.90.55.235']  # Define multiple hosts

    success_deploy = do_deploy(path)
    return success_deploy
