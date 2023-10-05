#!/usr/bin/python3
"""
This fabfile distributes an archive to my web servers
"""

import os
from fabric.api import *
from datetime import datetime


# Set the host IP addresses for web-01 && web-02
env.hosts = ['100.26.255.30', '100.25.191.160']
env.user = "ubuntu"


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # obtain the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Construct path where archive will be saved
    archive_path = "versions/web_static_{}.tgz".format(now)

    # use fabric function to create directory if it doesn't exist
    local("mkdir -p versions")

    # Use tar command to create a compresses archive
    archived = local("tar -cvzf {} web_static".format(archive_path))

    # Check archive Creation Status
    if archived.return_code != 0:
