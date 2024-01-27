#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
from os import stat


def do_pack():
    local('mkdir -p versions')
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_file = "versions/web_static_{}.tgz".format(timestamp)

    try:
        local('tar -cvzf "{}" ./web_static'.format(tgz_file))
        print("Generated tgz size:\t{}".format(stat(tgz_file).st_size))
    except Exception:
        tgz_file = None
    return tgz_file
