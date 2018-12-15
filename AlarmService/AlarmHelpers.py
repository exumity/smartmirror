# coding=utf-8
import json
import subprocess
import os
import signal
import threading

from DatabaseSmartMirror.DatabasePidsHelpers import Database as PidsDB
from PidNamesInterface import PidNames

from AlarmThreads.PlaySoundThread import PlaySoundThreadStart

from DatabaseSmartMirror.DatabaseObjreferencesHelpers import Database as RefDB
from ReferencesInterface import ReferenceNames

from ObjectGetter import Object as _Obj

alarm_ui_starting_process = None
alarm_sound_starting_process = None

alarm_sound_starting_thread = None
alarm_sound_starting_thread_stop = None


class AlarmHelpers(object):
    def startAlarmWidget(self, time_to_screen, ringing_time, alarm_ringtone_name):
        global alarm_ui_starting_process, alarm_sound_starting_process, \
            alarm_sound_starting_thread, alarm_sound_starting_thread_stop
        time_to_screen = str(time_to_screen)
        alarm_ui_starting_process = subprocess.Popen(
            ["sudo python /media/halildisk/SMARTMIRRORV2/MainUi.py alarm " + time_to_screen],
            stdout=subprocess.PIPE,
            preexec_fn=os.setsid,
            shell=True)


        ringing_alarm_pids = [(PidNames.getRingingAlarmUiPidName(), alarm_ui_starting_process.pid)]
        PidsDB().setPid(ringing_alarm_pids)

        alarm_sound_starting_thread_stop = threading.Event()
        alarm_sound_starting_thread = PlaySoundThreadStart(ringing_time, alarm_ringtone_name)
        alarm_sound_starting_thread.setDaemon(True)
        alarm_sound_starting_thread.start()


    def stopAlarmWidget(self):
        if not alarm_ui_starting_process == None:
            alarm_ui_process_pid = PidsDB().getPid(PidNames.getRingingAlarmUiPidName())
            os.killpg(os.getpgid(alarm_ui_process_pid), signal.SIGTERM)
            if not alarm_sound_starting_thread_stop == None:
                # os.killpg(os.getpgid(alarm_sound_starting_process.pid), signal.SIGTERM)

                # bu kısım %80 çalışmıyor thred içerisinden de dyrdyrdym
                alarm_sound_starting_thread_stop.set()
                alarm_sound_starting_thread.join()
        else:
            return False
