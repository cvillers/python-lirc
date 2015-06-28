# Demonstrates the low-level wrapper for liblirc_client.

import os
from lirc.internal import lirc_client

fd = lirc_client.lirc_get_local_socket(None, 1)

lirc_client.lirc_send_one(fd, "AC", "Power")

os.close(fd)