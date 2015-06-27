import lirc_client, os

fd = lirc_client.lirc_get_local_socket(None, 1)

lirc_client.lirc_send_one(fd, "AC", "Power")

os.close(fd)