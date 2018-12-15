# coding=utf-8
import serial
from PyQt4 import QtGui

from ReceiveData import ReceiveData
from Threads.SmartMirrorThreads import havadurumuThread, tarihvezamanThread, haberlerThread, sensorThread
from RestServices.GetWeathers import WeatherService
from RestServices.GetNews import NewsService
from LocalSystemServices.GetDateTime import DateTimeService

class widgetSmartMirror(QtGui.QWidget):
    def __init__(self, uiSM):
        QtGui.QWidget.__init__(self)
        self.ui=uiSM

    def appinit(self):
        thread = havadurumuThread()
        self.connect(thread, thread.signal, self.setNewWeatherThreadYeni)
        thread.start()

        thread0 = haberlerThread()
        self.connect(thread0, thread0.signal, self.setNewNewsThread)
        thread0.start()

        thread2 = tarihvezamanThread()
        self.connect(thread2, thread2.signal, self.setNewDateTime)
        thread2.start()

        thread3 = sensorThread()
        self.connect(thread3, thread3.signal, self.setSensor)

    def setNewDateTime(self):
        self.ui.setNewTime(DateTimeService().getDateTime()[0])
        self.ui.setNewDate(DateTimeService().getDateTime()[1])

    def setNewNewsThread(self):
        vals=NewsService().getNews()


        self.ui.setNewNewsVals(
            vals[0],
            vals[1],
            vals[2],
            vals[3],
            vals[4]
        )


    def setNewWeatherThreadYeni(self):
        vals=WeatherService().getDailyWeather()
        self.ui.setHighsLows(
            vals[0],
            vals[1],
            vals[2],
            vals[3],
            vals[4],
            vals[5],
            vals[6],
            vals[7],
            vals[8],
            vals[9],
            vals[10],
            vals[11],
            vals[12],
            vals[13],
            vals[14],
            vals[15],
            vals[16],
            vals[17],
            vals[18],
            vals[15]
        )
    def setSensor(self):
        #vals=ReceiveData().receiving()
        ser = serial.Serial('/dev/ttyACM0', 9600)
        ar = ser.readline()
        f=None
        if (ar != None):
            print(ar)
            f = ar.split(",")
            #self.sicaklik = str(f[4])
            #self.nem = str(f[5])
            if(len(f) == 6):
                self.ui.setSicaklikNem(
                    f[4],
                    f[5]
                )
            else:
                self.ui.setSicaklikNem(
                    "-",
                    "-"
                )
        else:
            self.ui.setSicaklikNem(
                "?",
                "?"
            )