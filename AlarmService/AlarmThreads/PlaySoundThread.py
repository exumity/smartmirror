import threading
import time
import os

import subprocess

import signal


class PlaySoundThreadStart(threading.Thread):
    def __init__(self, ringing_time,alarm_ringtone_name):
        threading.Thread.__init__(self)
        self.ringing_time = ringing_time
        self.alarm_ringtone_name=alarm_ringtone_name

    def run(self):
        counter=self.ringing_time
        process = subprocess.Popen(["sudo omxplayer -o local /media/halildisk/SMARTMIRRORV2/Sounds/"+self.alarm_ringtone_name],
                                   stdout=subprocess.PIPE
                                   , shell=True, preexec_fn=os.setsid)
        print("sound pid parent:" + str(process.pid) + " - " + str(os.getpgid(process.pid)))
        while counter > 0:
            if not process.poll() == None:
                process = subprocess.Popen(
                    ["sudo omxplayer -o local /media/halildisk/SMARTMIRRORV2/Sounds/"+self.alarm_ringtone_name],
                    stdout=subprocess.PIPE
                    , shell=True, preexec_fn=os.setsid)
                print("sound pid child:" + str(process.pid) + " - " + str(os.getpgid(process.pid)))
            counter = counter - 1
            time.sleep(1)

        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        exit(0)

