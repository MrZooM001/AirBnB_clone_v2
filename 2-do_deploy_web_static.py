#!/usr/bin/python3
"""A module that deploys an archive file to a web server."""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.25.111.4', '54.144.149.173']


def do_deploy(archive_path):
    """A function to distribute an archive to web servers using SSH"""
    if exists(archive_path) is False:
        return False
    
    try:
        file_name = archive_path.split("/")[-1]
        file_without_extention = file_name.split(".")[0]
        file_path = "/data/web_static/releases/"
        
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(file_path, file_without_extention))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file_name, file_path, file_without_extention))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(file_path, file_without_extention))
        run('sudo rm -rf {}{}/web_static'.format(file_path, file_without_extention))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(file_path, file_without_extention))
        return True
    except:
        return False
