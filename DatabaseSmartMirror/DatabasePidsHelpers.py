# coding=utf-8
import sqlite3 as sqlite

import os,inspect


class Database(object):

    def __init__(self):
        self.current_path = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))  # bu dosyanın bulunduğu path
        self.database_name = "smart_mirror_db_pids_temp.db"
        self.DB = sqlite.connect(str(self.current_path)+"/db/"+str(self.database_name))
        self.conn = self.DB.cursor()

        # Create table
        try:
            self.conn.execute('''
                            CREATE TABLE pids
                         (pid_name text, pid integer)
                         ''')
        except sqlite.Error:
            pass

    def __del__(self):
        try:
            self.conn.close()
            self.DB.close()
        except:
            pass
    def getPid(self,pid_name):
        t=(pid_name,)
        result = self.conn.execute(''' select pid from pids where pid_name=? ''', t).fetchall()
        if result.__len__() <= 0:
            return -1
        else:
            return result[0][0]
    #çoğul ekleme yapar daha önceden ekli olanı günceller
    #geliş değeri şu şekilde olmalı [('halil_pid',1024),('canavar_pid',5236)]
    def setPid(self,pids):
        t=pids
        if not pids.__len__() ==0:
            for (pid_name, pid) in pids:
                if self.checkPidNameIfExists(pid_name):
                    t=(pid,pid_name)
                    self.conn.execute(''' update pids set pid=? where pid_name=? ''',t)
                    self.DB.commit()
                else:
                    t = (pid_name,pid)
                    self.conn.execute(''' insert into pids (pid_name,pid) values (?,?) ''', t)
                    self.DB.commit()

        #self.conn.executemany(''' insert into pids (?,?) ''')

    def checkPidNameIfExists(self,pid_name):
        t=(pid_name,)
        count = self.conn.execute(''' select * from pids where pid_name=? ''',t).fetchall().__len__()
        if count >0:
            return True
        else:
            return False

    def deleteTable(self):
        self.conn.execute(''' drop table pids ''')

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
    Database().deleteTable()
    pids=[('halil_pid',10245),('canavar_pid',5236)]
    Database().setPid(pids)
    #Database().deleteTable()
    print(Database().getPid("halil_pid"))
'''

