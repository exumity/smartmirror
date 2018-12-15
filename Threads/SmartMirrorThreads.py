# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class tarihvezamanThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self, parent=None)
        self.signal = QtCore.SIGNAL("tarihvezamansinyali")
    def run(self):
        self.emit(self.signal, "tarihvezaman")


class havadurumuThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self, parent=None)
        self.signal = QtCore.SIGNAL("havadurumusinyali")
    def run(self):
        self.emit(self.signal, "havadurumu")




class haberlerThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self, parent=None)
        self.signal = QtCore.SIGNAL("haberlersinyali")
    def run(self):
        self.emit(self.signal, "haberler")

class sensorThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self, parent=None)
        self.signal = QtCore.SIGNAL("sensorsinyali")
    def run(self):
        self.emit(self.signal, "sensor")