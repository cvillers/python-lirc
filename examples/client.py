# Demonstrates usage of the lirc.client module.

from lirc.client import LircRemote

remote = LircRemote("AC")

remote.send_one("FanUp")
remote.send_one("FanDown")
