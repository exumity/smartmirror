# -*- coding: utf-8 -*-

#
# Halil Savaşcı
#

from PyQt4.QtCore import QTimer
from PyQt4 import QtCore, QtGui

from SmartMirrorForms.UiFormSM import Ui_Form,Ui_ComingCalls,Ui_AlarmRinging
from Widgets.WidgetSmartMirror import widgetSmartMirror


import sys
import locale


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "")


    if len(sys.argv) < 1:
        exit("parametre belirtilmedi")



    if str(sys.argv[1])=="main":
        app = QtGui.QApplication(sys.argv)
        ui = Ui_Form()
        widgetSM = widgetSmartMirror(ui)
        ui.setupUi(widgetSM)
        widgetSM.showFullScreen()

        QtCore.QTimer.singleShot(0, widgetSM.setNewDateTime)
        timer = QTimer()
        timer.timeout.connect(widgetSM.setNewDateTime)
        timer.setInterval(1000)  # 1 saniye
        timer.start()

        QtCore.QTimer.singleShot(0, widgetSM.setNewWeatherThreadYeni)
        timer2 = QTimer()
        timer2.timeout.connect(widgetSM.setNewWeatherThreadYeni)
        timer2.setInterval(3600000)  # 1 saat
        timer2.start()

        QtCore.QTimer.singleShot(0, widgetSM.setNewNewsThread)
        timer3 = QTimer()
        timer3.timeout.connect(widgetSM.setNewNewsThread)
        timer3.setInterval(300000)  # 10 dakika
        timer3.start()

        QtCore.QTimer.singleShot(0, widgetSM.setSensor)
        timer4 = QTimer()
        timer4.timeout.connect(widgetSM.setSensor)
        timer4.setInterval(1000)  # 1 saat
        timer4.start()

        sys.exit(app.exec_())
    elif sys.argv[1]=="incomingcall":
        app = QtGui.QApplication(sys.argv)
        ui2 = Ui_ComingCalls()
        widgetSM2 = widgetSmartMirror(ui2)
        ui2.setupUi(widgetSM2)
        widgetSM2.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ui2.setIncomingCallPersonName(str(sys.argv[2]))
        widgetSM2.show()
        sys.exit(app.exec_())
    elif sys.argv[1]=="alarm":
        app = QtGui.QApplication(sys.argv)
        ui2 = Ui_AlarmRinging()
        widgetSM3 = widgetSmartMirror(ui2)
        ui2.setupUi(widgetSM3)
        widgetSM3.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ui2.setAlarmTime(str(sys.argv[2]))
        widgetSM3.show()
        sys.exit(app.exec_())































