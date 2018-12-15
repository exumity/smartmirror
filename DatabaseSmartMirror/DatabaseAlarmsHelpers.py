# coding=utf-8
import sqlite3 as sqlite
import os
import inspect

class Database(object):
    def __init__(self):
        self.current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # bu dosyanın bulunduğu path
        self.database_name = "smart_mirror_alarms.db"
        self.DB = sqlite.connect(str(self.current_path)+"/db/"+str(self.database_name))
        self.conn = self.DB.cursor()


        # Create table
        try:
            self.conn.execute('''
                            CREATE TABLE alarms
                         (alarm_time text, ringtone integer, enable boolean)
                         ''')
        except sqlite.Error:
            pass

    def __del__(self):
        try:

            self.conn.close()
            self.DB.close()
        except:
            pass

    def getAllAlarms(self):

        result = self.conn.execute(''' select * from alarms ''').fetchall()
        if result.__len__() <= 0:
            return -1
        else:
            return result
    def getAllEnabledAlarms(self):
        t=(True,)
        result = self.conn.execute(''' select alarm_time,ringtone from alarms where enable=? ''', t).fetchall()
        if result.__len__() <= 0:
            return -1
        else:
            return result

    def enableAlarmDb(self,time):
        t = (True, str(time))
        self.conn.execute(''' update alarms set enable=?  where alarm_time=? ''', t)
        self.DB.commit()

    def disableAlarmDb(self,time):
        t = (False, str(time))
        self.conn.execute(''' update alarms set enable=? where alarm_time=? ''', t)
        self.DB.commit()


    #çoğul ekleme yapar daha önceden ekli olanı günceller
    #geliş değeri şu şekilde olmalı [('45:45','ringtone.mp3',True),]
    def setAlarm(self,alarms):
        t=alarms
        if not alarms.__len__() == 0:
            for (alarm_time, ringtone, enable) in alarms:
                if self.checkAlarmTimeIfExists(alarm_time):
                    t=(enable,ringtone,alarm_time)
                    self.conn.execute(''' update alarms set enable=?, ringtone=?  where alarm_time=? ''',t)
                    self.DB.commit()
                else:
                    t = (alarm_time,ringtone,enable)
                    self.conn.execute(''' insert into alarms (alarm_time,ringtone,enable) values (?,?,?) ''', t)
                    self.DB.commit()

        #self.conn.executemany(''' insert into pids (?,?) ''')

    def checkAlarmTimeIfExists(self,alarm_time):
        t=(alarm_time,)
        count = self.conn.execute(''' select * from alarms where alarm_time=? ''',t).fetchall().__len__()
        if count >0:
            return True
        else:
            return False

    def deleteAlarm(self,time):
        t=(time,)
        self.conn.execute(''' delete from alarms where alarm_time=? ''',t)
        self.DB.commit()

    def deleteTable(self):
        self.conn.execute(''' drop table alarms ''')

    def deleteDatabase(self):
        self.conn.close()
        self.DB.close()
        try:
            os.remove(str(self.current_path)+str(self.database_name))
            return True
        except OSError as e:
            return False



'''
if __name__=="__main__":
     #Database().getPid("halil")
     #Database().deleteTable()
     alarms=[('12:45','ring',True),('09:52','ring',True),('16:40','ring',True)]
     Database().setAlarm(alarms)
    # #Database().deleteTable()
    # print(Database().getAllEnabledAlarms())
     print(Database().getAllAlarms())

     Database().disableAlarmDb("09:52")

     print(Database().getAllAlarms())
    # Database().deleteAlarm("12:45")
    # print(Database().getAllAlarms())
'''

