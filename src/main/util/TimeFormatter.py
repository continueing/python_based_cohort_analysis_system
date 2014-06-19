from datetime import datetime

__author__ = 'continueing'



class TimeFormatter:
    DATETIME_STRING_FORMAT = '%Y-%m-%d %H:%M:%S'
    DATE_STRING_FORMAT = '%Y-%m-%d'

    @staticmethod
    def toDatetimeString(aDatetime):
        return aDatetime.strftime(TimeFormatter.DATETIME_STRING_FORMAT)

    @staticmethod
    def toDateString(aDatetime):
        return aDatetime.strftime(TimeFormatter.DATE_STRING_FORMAT)


    @staticmethod
    def toDatetime(aStringDatetime):
        return datetime.strptime(aStringDatetime,TimeFormatter.DATETIME_STRING_FORMAT)

