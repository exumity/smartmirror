#-*- coding: utf-8 -*-
import copy
from bluetooth import *
import threading
import time
from DatabaseSmartMirror.DatabaseObjreferencesHelpers import Database as RefsDB

from PyQt4.QtCore import QTimer
from PyQt4 import QtCore, QtGui

from ReferencesInterface import ReferenceNames
from SmartMirrorForms.UiFormSM import Ui_Form,Ui_ComingCalls
from Widgets.WidgetSmartMirror import widgetSmartMirror

from BluetoothThreads.ConnectionThread import BluetoothConnectionThread
from GpioHelpers.GpioHelperFunctions import GpioSmartMirrorHelpers

def initBluetoothSocketService():
    server_sock = BluetoothSocket(RFCOMM)

    server_sock.bind(("", PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]
    uuid = "85e017f5-0100-4c6c-9fb6-14d477163c86"

    advertise_service(server_sock, "SmartMirrorServer",
                      service_id=uuid,
                      service_classes=[uuid, SERIAL_PORT_CLASS],
                      profiles=[SERIAL_PORT_PROFILE],
                      #                   protocols = [ OBEX_UUID ]
                      )

    print("RFCOMM üzerinden baglanti bekleniyor... %d" % port)



    while True:
        client_sock, client_info = server_sock.accept()
        print(client_info, ": baglandi!")

        echo = BluetoothConnectionThread(client_sock, client_info)
        echo.setDaemon(True)
        echo.start()

    # server_sock.close()
    # client_sock.close()



if __name__ == "__main__":
    GpioSmartMirrorHelpers().initGpio()
    initBluetoothSocketService()




