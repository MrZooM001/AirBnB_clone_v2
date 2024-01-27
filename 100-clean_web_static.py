#!/usr/bin/python3
"""A module that clean out-dated archive files"""
from fabric.api import env, local, run, lcd, cd
from os import listdir
env.hosts = ['100.25.111.4', '54.144.149.173']


def do_clean(number=0):
    """A function that deletes out-of-date archives."""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(listdir("versions"))
    [archives.pop()for i in range(number)]

    with lcd("versions"):
        [local("sudo rm ./{}".format(arch)) for arch in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [arch for arch in archives if "web_static_" in arch]

        [archives.pop() for i in range(number)]        
        [run("sudo rm -rf ./{}".format(arch)) for arch in archives]
