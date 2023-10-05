#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from os.path import exists
env.hosts = ['100.26.232.13', '100.26.166.50']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Function to deploy"""
    if exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}/".format(path, name))
        run("sudo tar -xzf /tmp/{} -C {}{}/".format(file, path, name))
        run("sudo rm /tmp/{}".format(file))
        run("sudo mv {0}{1}/web_static/* {0}{1}/".format(path, name))
        run("sudo rm -rf {}{}/web_static".format(path, name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, name))
        return True
    except Exception:
        return False
