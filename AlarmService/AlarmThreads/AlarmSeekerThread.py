#-*- coding: utf-8 -*-


# THIS CLASS DEPRECATED - HALİL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import threading
import json

import os
import signal

from SoundService import PlaySound

from HelperFunctions.BluetoothSocketHelpers import BluetoothServerFunctions
import datetime

class AlarmSeekerThread(threading.Thread):
    def __init__(self, alarms):
        threading.Thread.__init__(self)
        self.alarms = alarms

    def run(self):
        try:
            while True:
                now = datetime.datetime.now()
                hour, minute, second = (now.hour, now.minute, now.second)

        except IOError:
            pass
        print(self.client_info, ": baglanti kesildi!")