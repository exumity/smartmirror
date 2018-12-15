# -*- coding: utf-8 -*-

import threading
import json

from HelperFunctions.BluetoothSocketHelpers import BluetoothServerFunctions



from ReferencesInterface import ReferenceNames
from DatabaseSmartMirror.DatabaseObjreferencesHelpers import Database as RefsDB

class BluetoothConnectionThread(threading.Thread):

    def __init__(self, sock, client_info):
        threading.Thread.__init__(self)
        self.sock = sock
        self.client_info = client_info



        if str(client_info[0]) != "14:1F:78:F9:12:62":
            self.sock.send("yousun...getout")
            self.sock.close()
            exit(0)



        #SharedSocket().setSocket(self.sock)

    def run(self):

        try:
            while True:
                data = self.sock.recv(1024)
                if len(data) == 0:
                    print("\nempty data came!!\n")
                    break
                print(self.client_info, ": gelen [%s]" % data)
                try:
                    data = json.loads(data)
                    if (data["from"] == "giris"):
                        BluetoothServerFunctions().authenticate(self.sock, data)


                    elif (data["from"] == "list_wifi"):
                        BluetoothServerFunctions().scanWifi(self.sock)

                    elif (data["from"] == "connect_wifi"):
                        BluetoothServerFunctions().connectWifi(self.sock, data)

                    elif (data["from"] == "shutdown_mirror"):
                        BluetoothServerFunctions().shutDownSmartMirror(self.sock, data)

                    elif (data["from"] == "led_state"):
                        BluetoothServerFunctions().getLedState(self.sock)
                    elif (data["from"] == "stop_sensor_stream"):
                        BluetoothServerFunctions().getLedState(self.sock)

                    elif (data["from"] == "incoming_call_started"):
                        BluetoothServerFunctions().incomingCallStarted(data)

                    elif (data["from"] == "incoming_call_finished"):
                        BluetoothServerFunctions().incomingCallFinished()

                    elif (data["from"] == "change_led_state"):
                        BluetoothServerFunctions().changeLedState(self.sock)
                    elif (data["from"] == "sensor_anasayfa_degerler"):
                        BluetoothServerFunctions().sensorlerAnadegerler(self.sock)
                    elif (data["from"] == "sensorler_sicaklik_degerler"):
                        BluetoothServerFunctions().sicaklikSensorDegerleri(self.sock)
                    elif (data["from"] == "sensorler_nem_degerler"):
                        BluetoothServerFunctions().nemSensorDegerleri(self.sock)
                    elif (data["from"] == "sensorler_su_degerler"):
                        BluetoothServerFunctions().suSensorDegerleri(self.sock)
                    elif (data["from"] == "sensorler_gaz_degerler"):
                        BluetoothServerFunctions().gazSensorDegerleri(self.sock)
                    elif (data["from"] == "sensorler_hareket_degerler"):
                        BluetoothServerFunctions().hareketSensorDegerleri(self.sock)
                    elif (data["from"] == "alarmlar"):
                        BluetoothServerFunctions().alarmDegerleri(self.sock)
                    elif (data["from"] == "set_new_alarm"):
                        BluetoothServerFunctions().alarmEkle(self.sock, data)
                    elif (data["from"] == "delete_alarm"):
                        BluetoothServerFunctions().alarmSil(self.sock, data)
                    elif (data["from"] == "enable_alarm"):
                        BluetoothServerFunctions().alarmEnabled(self.sock, data)
                    elif (data["from"] == "disable_alarm"):
                        BluetoothServerFunctions().alarmDisabled(self.sock, data)


                except ValueError, e:
                    if data == "iwannaconnect":
                        senddata = "metoo"
                        self.sock.send(senddata)
                        print(self.client_info, ": giden [%s]" % senddata)
                    else:
                        self.sock.close()
                        print("illegal yontem tespit edildi!!! =>" + str(e))
        except IOError:
            pass
        self.sock.close()
        print(self.client_info, ": baglanti kesildi!")
