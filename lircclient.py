"""
Client interface to LIRC using SWIG (see swig/ directory for more details).
"""

import lirc_client, os

class LircError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

class LircClient:
    """
    Low-level LIRC client. Wraps related functions.

    :type fd: int
    """
    def __init__(self, socket=None, quiet=True):
        fd = lirc_client.lirc_get_local_socket(socket, quiet)

        if fd < 0:
            raise LircError("Error while connecting to LIRC: {0}".format(os.strerror(-fd)))

        self.fd = fd

    def __del__(self):
        os.close(self.fd)

    def send_one(self, remote, button):
        """
        Synchronously sends a button one time.
        :param str remote: Name of the remote.
        :param str button: Name of the button.
        """
        if lirc_client.lirc_send_one(self.fd, remote, button) == -1:
            raise RuntimeError("Error while communicating with LIRC daemon!")

class LircRemote:
    """
    High-level wrapper around LIRC remotes.

    :type name: str
    """

    def __init__(self, name):
        """
        Initializes the instance.
        :param str name: The remote name.
        """
        self.name = name
        self.client = LircClient()

    def send_one(self, button):
        """
        Synchronously sends a button one time.
        :param str button: The button name.
        """
        self.client.send_one(self.name, button)