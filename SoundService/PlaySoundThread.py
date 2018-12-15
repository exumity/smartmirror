import threading
import time
import os

import subprocess


class PlaySoundThreadStart(threading.Thread):
    def __init__(self, ringing_time):
        threading.Thread.__init__(self)
        self.ringing_time = ringing_time

    def run(self):
        process = subprocess.Popen(["sudo omxplayer -o local /media/halildisk/SMARTMIRRORV2/Sounds/ringtone.mp3"],
                                   stdout=subprocess.PIPE
                                   , shell=True, preexec_fn=os.setsid)
        print("sound pid:" + str(process.pid) + " - " + str(os.getpgid(process.pid)))
        while self.ringing_time > 0:
            if not process.poll() == None:
                process = subprocess.Popen(
                    ["sudo omxplayer -o local /media/halildisk/SMARTMIRRORV2/Sounds/ringtone.mp3"],
                    stdout=subprocess.PIPE
                    , shell=True, preexec_fn=os.setsid)
                print("sound pid:" + str(process.pid) + " - " + str(os.getpgid(process.pid)))
            self.ringing_time -= 1
            time.sleep(1)

        # return os.getpgid(process.pid)
        return True