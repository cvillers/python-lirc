"""
Client interface to LIRC using FFI.
"""

from ctypes import *

liblirc_client = CDLL("liblirc_client.so.0")

lirc_get_local_socket = CFUNCTYPE(c_int, c_char_p, c_int)("lirc_get_local_socket", liblirc_client)

def get_local_socket(path, quiet):
    """
    Return an opened and connected file descriptor to local lirc socket.
    :param str or None path: Path to socket. If None use LIRC_SOCKET_PATH in environment.
    :param bool quiet: If true, don't write error messages on stderr.
    :rtype: int
    :return: Positive file descriptor on success, else a negated kernel error code.
    """

    # FIXME ASCII is probably ok, but locale.getpreferredencoding() is the Right Thing To Do
    param_path = c_char_p(path.encode("ASCII") if path is not None else None)
    param_quiet = c_int(1 if quiet else 0)

class LircClient:
    def __init__(self):
        self.fd = get_local_socket(None, False)

    def send_once(self, remote, button):
        """
        Sends a button one time.
        :param str remote: Name of the remote.
        :param str button: Name of the button.
        :return:
        """
        pass