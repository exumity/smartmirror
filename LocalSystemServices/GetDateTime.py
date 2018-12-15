# -*- coding: utf-8 -*-

import datetime




class DateTimeService(object):
    def getDateTime(self):
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

        now_date_string = datetime.datetime.now().strftime("%A %d %B %Y")  # %A %d %B %Y
        time_now = hour + ":" + minute + ":" + second

        return (time_now,now_date_string)

