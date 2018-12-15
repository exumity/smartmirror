# -*- coding: utf-8 -*-

import json
import time
import subprocess

import datetime

import signal

import os

from PidNamesInterface import PidNames
from GpioHelpers.GpioHelperFunctions import GpioSmartMirrorHelpers

from DatabaseSmartMirror.DatabaseAlarmsHelpers import Database as AlarmDB

from DatabaseSmartMirror.DatabasePidsHelpers import Database as PidsDB

from AlarmService.AlarmHelpers import AlarmHelpers

# yeni versiyonlarda bunu murderer ile yap :) ;)
incoming_call_pid = 0

class BluetoothServerFunctions(object):
    def alarmDisabled(self, sock, alarm):
        alarm = alarm["alarm"]
        alarm_time = str(alarm["time"])
        AlarmDB().disableAlarmDb(alarm_time)

        # eğer alarmservisi çalışıyor ise restartla çalışmıyorsa çalıştır
        # eğer buişlem yapılıyorken alarm çalışıyorsa ilk önce onu durdur
        alarm_service_pid = PidsDB().getPid(PidNames.getAlarmServicePidName())
        # print(alarm_service_pid)
        AlarmHelpers().stopAlarmWidget()
        if not alarm_service_pid == -1:
            # tam yetkiyle girdiğimiziçin bu pidde program çalışmıyo ise sonlandıramaz
            # sonlandıramıyosa demekki zaten process çalşımıyordur
            try:
                os.killpg(os.getpgid(alarm_service_pid), signal.SIGTERM)
            except OSError:
                pass
            alarm_service_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/AlarmService/AlarmService.py "], shell=True,
                preexec_fn=os.setsid)
            PidsDB().setPid([(PidNames.getAlarmServicePidName(), alarm_service_process.pid)])
        else:
            alarm_service_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/AlarmService/AlarmService.py "],
                shell=True, preexec_fn=os.setsid)
            PidsDB().setPid([(PidNames.getAlarmServicePidName(), alarm_service_process.pid)])

        self.alarmDegerleri(sock)

    def alarmEnabled(self, sock, alarm):
        alarm = alarm["alarm"]
        alarm_time = str(alarm["time"])
        AlarmDB().enableAlarmDb(alarm_time)

        # eğer alarmservisi çalışıyor ise restartla çalışmıyorsa çalıştır
        # eğer buişlem yapılıyorken alarm çalışıyorsa ilk önce onu durdur
        alarm_service_pid = PidsDB().getPid(PidNames.getAlarmServicePidName())
        # print(alarm_service_pid)
        AlarmHelpers().stopAlarmWidget()
        if not alarm_service_pid == -1:
            # tam yetkiyle girdiğimiziçin bu pidde program çalışmıyo ise sonlandıramaz
            # sonlandıramıyosa demekki zaten process çalşımıyordur
            try:
                os.killpg(os.getpgid(alarm_service_pid), signal.SIGTERM)
            except OSError:
                pass
            alarm_service_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/AlarmService/AlarmService.py "], shell=True,
                preexec_fn=os.setsid)
            PidsDB().setPid([(PidNames.getAlarmServicePidName(), alarm_service_process.pid)])
        else:
            alarm_service_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/AlarmService/AlarmService.py "],
                shell=True, preexec_fn=os.setsid)
            PidsDB().setPid([(PidNames.getAlarmServicePidName(), alarm_service_process.pid)])

        self.alarmDegerleri(sock)

    def alarmSil(self, sock, alarm):
        alarm = alarm["alarm"]
        alarm_time = str(alarm["time"])
        AlarmDB().deleteAlarm(alarm_time)

        # eğer alarmservisi çalışıyor ise restartla çalışmıyorsa çalıştır
        # eğer buişlem yapılıyorken alarm çalışıyorsa ilk önce onu durdur
        alarm_service_pid = PidsDB().getPid(PidNames.getAlarmServicePidName())
        # print(alarm_service_pid)
        AlarmHelpers().stopAlarmWidget()
        if not alarm_service_pid == -1:
            # tam yetkiyle girdiğimiziçin bu pidde program çalışmıyo ise sonlandıramaz
            # sonlandıramıyosa demekki zaten process çalşımıyordur
            try:
                os.killpg(os.getpgid(alarm_service_pid), signal.SIGTERM)
            except OSError:
                pass
            alarm_service_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/AlarmService/AlarmService.py "], shell=True,
                preexec_fn=os.setsid)
            PidsDB().setPid([(PidNames.getAlarmServicePidName(), alarm_service_process.pid)])
        else:
            alarm_service_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/AlarmService/AlarmService.py "],
                shell=True, preexec_fn=os.setsid)
            PidsDB().setPid([(PidNames.getAlarmServicePidName(), alarm_service_process.pid)])

        self.alarmDegerleri(sock)

    def alarmEkle(self, sock, alarm):
        alarm = alarm["alarm"]
        alarm_time = str(alarm["saat"]) + ":" + str(alarm["dakika"])
        alarm_ringtone = alarm["ringtone"]
        alarm_enable = True
        _alarm = [(alarm_time, alarm_ringtone, alarm_enable)]
        AlarmDB().setAlarm(_alarm)
        now = datetime.datetime.now()
        now_hour, now_minute = (now.hour, now.minute)
        over_hour = int(alarm["saat"]) - int(now_hour)
        over_minute = int(alarm["dakika"]) - int(now_minute)

        # kalan zamanı hesaplayıp string hale getirme
        if over_hour < 0:
            over_hour = 24 + int(over_hour)

        if over_minute < 0:
            over_hour = over_hour - 1
            if over_hour < 0:
                over_hour = 24 - int(over_hour)
            over_minute = 60 + int(over_minute)

        over_message = ""
        if not over_hour == 0:
            over_message += str(over_hour) + " saat "
        if not over_minute == 0:
            over_message += str(over_minute) + " dakika "

        over_message += "sonrasına alarm kuruldu."

        # eğer alarmservisi çalışıyor ise restartla çalışmıyorsa çalıştır
        # eğer buişlem yapılıyorken alarm çalışıyorsa ilk önce onu durdur
        alarm_service_pid = PidsDB().getPid(PidNames.getAlarmServicePidName())
        # print(alarm_service_pid)
        AlarmHelpers().stopAlarmWidget()
        if not alarm_service_pid == -1:
            # tam yetkiyle girdiğimiziçin bu pidde program çalışmıyo ise sonlandıramaz
            # sonlandıramıyosa demekki zaten process çalşımıyordur
            try:
                os.killpg(os.getpgid(alarm_service_pid), signal.SIGTERM)
            except OSError:
                pass
            alarm_service_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/AlarmService/AlarmService.py "], shell=True,
                preexec_fn=os.setsid)
            PidsDB().setPid([(PidNames.getAlarmServicePidName(), alarm_service_process.pid)])
        else:
            alarm_service_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/AlarmService/AlarmService.py "],
                shell=True, preexec_fn=os.setsid)
            PidsDB().setPid([(PidNames.getAlarmServicePidName(), alarm_service_process.pid)])

        result = {"to": "new_alarm_set", "data": {"message": str(over_message)}}

        # result='{"to":"new_alarm_set","data":{"message":"'+over_message+'"}}'
        print(result)
        sock.send(json.dumps(result))
        self.alarmDegerleri(sock)

    def alarmDegerleri(self,sock):

        try:
            data = AlarmDB().getAllAlarms()  # v2

            print(data)

            result_data = []
            if data == -1:
                result_data = []
            else:
                for (time, ringtone, enabled) in data:
                    saat = str(time).split(":")[0]
                    dakika = str(time).split(":")[1]
                    if enabled == 1:
                        result_data.append({'saat': str(saat), 'dakika': str(dakika), 'durum': 'true'})
                    else:
                        result_data.append({'saat': str(saat), 'dakika': str(dakika), 'durum': 'false'})

            result = '{"alarmdegerleri":' + json.dumps(result_data) + '}'
            # data = json.load(open("/media/halildisk/jsonsDB/Alarmlar.json")) #v1
            result = '{"to":"alarmlar","data":' + result + '}'
            sock.send(result)
        except IOError, e:
            print(e)

    def hareketSensorDegerleri(self, sock):
        try:
            data = json.load(open("/media/halildisk/jsonsDB/HareketDegerler.json"))
            result = '{"to":"sensorler_hareket_degerler","data":' + json.dumps(data) + '}'
            print(result)
            sock.send(result)
        except IOError, e:
            print(e)

    def suSensorDegerleri(self, sock):
        try:
            data = json.load(open("/media/halildisk/jsonsDB/SuDegerler.json"))
            result = '{"to":"sensorler_su_degerler","data":' + json.dumps(data) + '}'
            print(result)
            sock.send(result)
        except IOError, e:
            print(e)

    def nemSensorDegerleri(self, sock):
        try:
            data = json.load(open("/media/halildisk/jsonsDB/NemDegerleri.json"))
            result = '{"to":"sensorler_nem_degerler","data":' + json.dumps(data) + '}'
            print(result)
            sock.send(result)
        except IOError, e:
            print(e)

    def gazSensorDegerleri(self, sock):
        try:
            data = json.load(open("/media/halildisk/jsonsDB/GazDegerleri.json"))
            result = '{"to":"sensorler_gaz_degerler","data":' + json.dumps(data) + '}'
            print(result)
            sock.send(result)
        except IOError, e:
            print(e)

    def sicaklikSensorDegerleri(self, sock):
        try:
            data = json.load(open("/media/halildisk/jsonsDB/SicaklikDegerleri.json"))
            result = '{"to":"sensorler_sicaklik_degerler","data":' + json.dumps(data) + '}'
            print(result)
            sock.send(result)
        except IOError, e:
            print(e)

    def sensoranadegerlerStreamStop(self):
        global sensorstream
        sensorstream = False

    def sensoranadegerlerStream(self, sock):
        global sensorstream
        sensorstream = True
        sayac = True
        while True:
            if not sensorstream:
                break
            time.sleep(2)
            if sayac:
                data = json.load(open("/media/halildisk/jsonsDB/EnsonSensorDegerleri2.json"))
                result = '{"to":"sensorler_anasayfa","data":' + json.dumps(data) + '}'
                print(result)
                sock.send(result)
                sayac = False
            else:
                data = json.load(open("/media/halildisk/jsonsDB/EnsonSensorDegerleri.json"))
                result = '{"to":"sensorler_anasayfa","data":' + json.dumps(data) + '}'
                print(result)
                sock.send(result)
                sayac = True

    def sensorlerAnadegerler(self, sock):
        try:
            data = json.load(open("/media/halildisk/jsonsDB/EnsonSensorDegerleri.json"))
            result = '{"to":"sensorler_anasayfa","data":' + json.dumps(data) + '}'
            print(result)
            sock.send(result)
        except IOError, e:
            print(e)

    def shutDownSmartMirror(self, sock, data):
        try:
            result = "{\"to\":\"shutdown_mirror\",\"message\":\"OK\"}"
            sock.send(result)
            print(result)
            time.sleep(2)
            p = subprocess.call("sudo poweroff", shell=True)


        except:
            print("shutdown istegi basarisiz")

    def changeLedState(self, sock):
        GpioSmartMirrorHelpers().changeSMLedState()
        result = '{"to":"change_led_state","message":"OK"}'
        sock.send(result)
        print(result)

    def getLedState(self, sock):
        try:
            led_state = GpioSmartMirrorHelpers().getSMLedState()
            if (led_state):
                response = '{"to":"led_state","state":true}'
            else:
                response = '{"to":"led_state","state":false}'
            sock.send(response)
            print(response)
        except ValueError, e:
            print("led state gonderilemedi")

    def authenticate(self, sock, data):
        db_username = "halil"
        db_password = "1234"
        send_data = "OOPS"

        if data["username"] == db_username and data["password"] == db_password:
            send_data = "AUTH_OK"
        else:
            send_data = "AUTH_FAILED"
        sock.send(send_data)

    def checkConnectedEthernet(self):
        try:
            wifis = subprocess.check_output("sudo iwgetid wlan0 | grep ESSID", shell=True)
            wifis = wifis.split("\"")
            ssid = wifis[1]
            if (ssid == ""):
                return ""
            else:
                r = ssid.replace("\"", "")
                return r
        except ValueError, e:
            return ""

    def scanWifi(self, socket):
        wifis = subprocess.check_output("sudo iwlist wlan0 scan | grep ESSID", shell=True)
        wifis = wifis.strip()
        wifis = wifis.replace(" ", "")
        wifis = wifis.replace("\"", "")
        wifis_array = wifis.split("\n")

        wifi_essids = []
        for w in wifis_array:
            wifi_essids.append(w.split(":")[1])

        raw_json = json.dumps(wifi_essids)
        result = '{"to":"wifi_list","wifi_names":' + raw_json + ',"connected":"' + self.checkConnectedEthernet() + '"}'
        socket.send(result)
        print(result)

    def connectWifi(self, socket, data):
        if (data["from"] == "connect_wifi"):
            command_line = "wpa_passphrase " + data['name'] + " " + data[
                'pass'] + " | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"
            p = subprocess.call(command_line, shell=True)
            p = subprocess.call("wpa_cli -i wlan0 reconfigure", shell=True)
            # args = shlex.split(command_line)
            # p = subprocess.Popen(args)
            socket.send("{'to':'wifi_connected','message':'ok'}")
            print(p)

            time.sleep(9)


            mainui_pid = PidsDB().getPid(PidNames.getMainUiPidName())
            os.killpg(os.getpgid(mainui_pid), signal.SIGTERM)
            #ui restart
            main_ui_process = subprocess.Popen(
                ["sudo python /media/halildisk/SMARTMIRRORV2/MainUi.py \"main\""],
                shell=True,
                preexec_fn=os.setsid
            )
            pids = [
                (PidNames.getMainUiPidName(), main_ui_process.pid)
            ]
            PidsDB().setPid(pids)


    def incomingCallStarted(self, data):
        global incoming_call_pid
        who = str(data["who"])
        process = subprocess.Popen(["python /media/halildisk/SMARTMIRRORV2/MainUi.py incomingcall " + who], shell=True,
                                   preexec_fn=os.setsid)
        incoming_call_pid = process.pid
        calling_pid = [(PidNames.getRingingCallPidName(), incoming_call_pid)]
        PidsDB().setPid(calling_pid)
        print(incoming_call_pid)

    def incomingCallFinished(self):
        print(incoming_call_pid)
        ringingcall_pid = PidsDB().getPid(PidNames.getRingingCallPidName())
        os.killpg(os.getpgid(ringingcall_pid), signal.SIGTERM)
        # process = subprocess.Popen(["sudo kill " + str(incoming_call_pid)], shell=True)
        # process2 = subprocess.Popen(["sudo kill "+str(incoming_call_pid+1)], shell=True)
        # process.terminate()
        # process2.terminate()
