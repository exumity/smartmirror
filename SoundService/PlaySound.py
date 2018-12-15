# coding:utf-8
import time

import os
import signal
import subprocess

#DEPRECATED FOR NOW - !!!!!!!!!!!!!!!!!!!!!

class PlaySound(object):
    def playRingtone(self,sound_timeout):#saniye cinsiden gelmeli
        process = subprocess.Popen(["sudo omxplayer -o local /media/halildisk/SMARTMIRRORV2/Sounds/ringtone.mp3"],
                                   stdout=subprocess.PIPE
                                   , shell=True, preexec_fn=os.setsid)
        print("sound pid:" + str(process.pid) + " - " + str(os.getpgid(process.pid)))
        while sound_timeout>0:
            if not process.poll() == None:
                process = subprocess.Popen(
                    ["sudo omxplayer -o local /media/halildisk/SMARTMIRRORV2/Sounds/ringtone.mp3"],
                    stdout=subprocess.PIPE
                    , shell=True, preexec_fn=os.setsid)
                print("sound pid:" + str(process.pid) + " - " + str(os.getpgid(process.pid)))
            sound_timeout -= 1
            time.sleep(1)



        #return os.getpgid(process.pid)
        return True

        #os.killpg(os.getpgid(process.pid), signal.SIGTERM)

