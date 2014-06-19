from src.main.domain.Period import Period
from src.main.domain.UserBehavior import UserBehavior
from src.main.network_communication.ClassweekHttpRequester import ClassweekHttpRequester
from src.main.util.RelativeProjectPathManager import  RelativeProjectPathManager
from src.main.util.TimeFormatter import TimeFormatter


__author__ = 'continueing'

import csv, os
from datetime import datetime

class Group:
    #Column order: id -> startDateString -> endDateString -> savedDateTime
    FILE_PATH_TO_SAVE = '/resource/group.csv'
    savedDateTime = None


    def __init__(self, anId, aStartDate, anEndDate, aNickname, savedDateTime=None):
        self.id = anId
        self.period = Period(aStartDate,anEndDate)
        self.nickName = aNickname
        if(savedDateTime is not None):
            self.savedDateTime = savedDateTime


    @staticmethod
    def fromCSVRow(aRow):
        id = int(aRow.pop(0))
        period = Period( TimeFormatter.toDatetime( aRow.pop(0) ), TimeFormatter.toDatetime( aRow.pop(0) ))
        nickName = aRow.pop(0)
        savedDateTime = TimeFormatter.toDatetime(aRow.pop(0))
        result = Group(id,period.start,period.end,nickName,savedDateTime)
        return result


    @staticmethod
    def all():
        result = []
        if(RelativeProjectPathManager.isThereFile(Group.FILE_PATH_TO_SAVE)):
            with open(RelativeProjectPathManager.getRealFilePathToSave(Group.FILE_PATH_TO_SAVE), 'r', encoding='UTF8') as rCSVFile:
                reader = csv.reader(rCSVFile, delimiter=',')
                for row in reader:
                    result.append(Group.fromCSVRow(aRow=row))
        return result

    @staticmethod
    def findById(anId):
        result = None
        if(RelativeProjectPathManager.isThereFile(Group.FILE_PATH_TO_SAVE)):
            with open(RelativeProjectPathManager.getRealFilePathToSave(Group.FILE_PATH_TO_SAVE), 'r', encoding='UTF8') as rCSVFile:
                reader = csv.reader(rCSVFile, delimiter=',')
                for row in reader:
                    group = Group.fromCSVRow(row)
                    if(group.id == anId):
                        result = group
                        break
                rCSVFile.close()
        return result



    def __eq__(self, other):
        if(self.id != other.id):
            return  False
        if(self.nickName != other.nickName):
            return False
        if(self.period != other.period):
            return False
        else:
            return True

    def save(self):
        if(Group.findById(self.id) is not None):
            Group.delete(self.id)

        with open(RelativeProjectPathManager.getRealFilePathToSave(Group.FILE_PATH_TO_SAVE), 'a', encoding='UTF8') as wCSVFile:
            writer = csv.writer(wCSVFile, delimiter=',')
            row = []
            row.append(self.id)
            row.append(TimeFormatter.toDatetimeString(self.period.start))
            row.append(TimeFormatter.toDatetimeString(self.period.end))
            row.append(self.nickName)
            self.savedDateTime = datetime.now()
            row.append(TimeFormatter.toDatetimeString(self.savedDateTime))
            writer.writerow(row)
            wCSVFile.close()


    def isSavedOne(self):
        if(self.savedDateTime == None):
            return False
        else:
            return True

    @staticmethod
    def delete(anIndex):
        if(RelativeProjectPathManager.isThereFile(Group.FILE_PATH_TO_SAVE)):
            groups = Group.all()
            for groupTuple in enumerate(groups):
                if(groupTuple[1].id == anIndex):
                    groups.pop(groupTuple[0])

            os.remove(RelativeProjectPathManager.getRealFilePathToSave(Group.FILE_PATH_TO_SAVE))
            with open(RelativeProjectPathManager.getRealFilePathToSave(Group.FILE_PATH_TO_SAVE), 'w', encoding='UTF8') as wCSVFile:
                writer = csv.writer(wCSVFile, delimiter=',')
                for group in groups:
                    row = []
                    row.append(group.id)
                    row.append(TimeFormatter.toDatetimeString(group.period.start))
                    row.append(TimeFormatter.toDatetimeString(group.period.end))
                    row.append(group.nickName)
                    row.append(TimeFormatter.toDatetimeString(group.savedDateTime))
                    writer.writerow(row)
                    wCSVFile.close()


    def retrieveSessionIds(self):
        return ClassweekHttpRequester.getSessionIdsGivenPeriod(self.period)
