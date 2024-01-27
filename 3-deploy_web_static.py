#!/usr/bin/python3
"""A module that deploys an archive file to a web server."""
from fabric.api import env, local, put, run
from datetime import datetime
from os import stat
from os.path import exists
env.hosts = ['100.25.111.4', '54.144.149.173']


def do_pack():
    """A function to compress a web static files into .tgz archive file."""
    local('mkdir -p versions')
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_file = "versions/web_static_{}.tgz".format(timestamp)
    try:
        local('tar -cvzf "{}" ./web_static'.format(tgz_file))
        print("Generated tgz size:\t{}".format(stat(tgz_file).st_size))
    except Exception:
        tgz_file = None
    return tgz_file


def do_deploy(archive_path):
    """A function to distribute an archive to web servers using SSH"""
    if exists(archive_path) is False:
        return False

    try:
        fName = archive_path.split("/")[-1]
        noExt = fName.split(".")[0]
        fPath = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(fPath, noExt))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(fName, fPath, noExt))
        run('sudo rm /tmp/{}'.format(fName))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(fPath, noExt))
        run('sudo rm -rf {}{}/web_static'.format(fPath, noExt))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(fPath, noExt))
        return True
    except Exception:
        return False


def deploy():
    """A function to deploy a web static"""
    path = do_pack()
    if (path is None):
        return False
    try:
        local('ls {}'.format(path))
    except Exception:
        return False
    return do_deploy(path)
