# coding=utf-8
# Halil Savaşcı
import ctypes
import datetime
import json
import time



"""
Eğer bu dosya direkt çağrılırsa sys path burdan başlıcağı için 
eksik packagelar mevcut olmakta o yüzden direkt çağrımlar için burda sys path 
ekleme işlemi yapılıyor
"""
from os.path import dirname
import sys
# base path varma işlemi her init dosyası için farklılık gösterebilir onu iyi ayarlamak lazım
current_folder = dirname(dirname(__file__))
base_path = current_folder

is_set_path = False
for path in sys.path:
    if path == base_path:
        is_set_path = True


sys.path.append(base_path)

from ReferencesInterface import ReferenceNames

from DatabaseSmartMirror.DatabaseAlarmsHelpers import Database as AlarmsDB
from DatabaseSmartMirror.DatabaseObjreferencesHelpers import Database as RefDB

from ObjectGetter import Object as _Obj

from AlarmHelpers import AlarmHelpers



class AlarmService:

    def __init__(self):
        pass

    def main(self):
        alarms = AlarmsDB().getAllEnabledAlarms()
        #print(alarms)
        if alarms == -1:
            print("alarm servisi çıkış yaptı")
            exit()

        ringing_second = 30

        # aynı zamandaki alarmın günde bir defa çalması için
        time_unique = None
        time_unique_passed = None
        while True:
            now = datetime.datetime.now()

            hour, minute, second = (now.hour, now.minute, now.second)
            if hour < 10:
                hour = "0" + str(hour)
            else:
                hour = str(hour)
            if minute < 10:
                minute = "0" + str(minute)
            else:
                minute = str(minute)
            if second < 10:
                second = "0" + str(second)
            else:
                second = str(second)

            alarm_hour = ""
            alarm_minute = ""

            for (alarm_time, alarm_ringtone_name) in alarms:
                alarm_hour = str(alarm_time.split(":")[0])
                alarm_minute = str(alarm_time.split(":")[1])
                time_unique = str(now.year) + str(now.month) + str(now.day) + str(alarm_hour) + str(alarm_minute)

                # alarm ui tetiklenmeli
                if alarm_hour == hour and alarm_minute == minute:
                    # eğer daha önce çalmadıysa çal
                    if not str(time_unique_passed) == str(time_unique):
                        time_unique_passed = str(time_unique)
                        # print("tq_in: " + str(time_unique))
                        time_to_go = hour + ":" + minute
                        print("alarm\n")

                        AlarmHelpers().startAlarmWidget(time_to_go, ringing_second, alarm_ringtone_name)
                        time.sleep(ringing_second)
                        AlarmHelpers().stopAlarmWidget()

            time.sleep(1)


if __name__ == "__main__":
    AlarmService().main()
