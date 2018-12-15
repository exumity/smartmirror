import serial


class ReceiveData(object):
    def receiving(self):
        ser =serial.Serial('/dev/ttyACM0',9600)
        while True:
            ar = ser.readline()
            f=ar.split(",")
            if(ar != None):
                self.isik=str(f[0])
                print(self.isik)
                self.gaz=str(f[1])
                self.su=str(f[2])
                self.hareket=str(f[3])
                self.sicaklik=str(f[4])
                self.nem=str(f[5])

if __name__== "__main__":
    ReceiveData().receiving()
