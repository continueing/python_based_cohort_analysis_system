__author__ = 'continueing'
import os


class RelativeProjectPathManager():

    PROJECT_NAME = 'ClassweekCohort'

    @staticmethod
    def getRootPath():
        currentPath = os.path.abspath('.').split('/')
        rootPath=''
        for directoryName in currentPath:
            if(directoryName != ''):
                rootPath += '/' + directoryName
            if(directoryName == RelativeProjectPathManager.PROJECT_NAME):
                break
        return rootPath

    @staticmethod
    def isThereFile(aRelativeFilePath):
        return os.path.isfile(RelativeProjectPathManager.getRootPath() + aRelativeFilePath)

    @staticmethod
    def getRealFilePathToSave(aRelativeFilePath):
        return RelativeProjectPathManager.getRootPath() + aRelativeFilePath


