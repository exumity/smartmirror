
class PidNames(object):
    @staticmethod
    def getMainUiPidName():
        return str("mainui_pid")

    @staticmethod
    def getSocketServicePidName():
        return str("socketservice_pid")

    @staticmethod
    def getAlarmServicePidName():
        return str("alarmservice_pid")

    @staticmethod
    def getRingingCallPidName():
        return str("ringingcall_pid")

    @staticmethod
    def getRingingAlarmUiPidName():
        return str("ringingalarmui_pid")