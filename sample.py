import lircclient

remote = lircclient.LircRemote("AC")

remote.send_one("TempTimerUp")
remote.send_one("FanDown")
