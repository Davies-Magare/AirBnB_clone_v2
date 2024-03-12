#!/usr/bin/python3
from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['35.174.208.95']
env.key_filename = '~/.ssh/school'

def run_script():
    local("scp -i {} 0-setup_web_static.sh ubuntu@{}:~".format(env.key_filename, env.hosts))
    run("chmod u+x 0-setup_web_static.sh")
    sudo("./0-setup_web_static.sh")
    run("echo $?")
def view_nginx_status():
    run("ls -l /data")
    run("ls -l /data/web_static")
    run("cat /data/web_static/current/index.html")
    run("curl localhost/hbnb_static/index.html")
    run("echo $?")
def run_tasks():
    run_script()
    view_nginx_status()
