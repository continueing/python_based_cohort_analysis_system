
from src.main.network_communication.ClassweekHttpRequester import ClassweekHttpRequester
import json
from src.main.util.RelativeProjectPathManager import RelativeProjectPathManager

__author__ = 'continueing'


directoryPathToSave = '/src/test/resource'

def saveUserLog(aSessionId, aFileName):
    with open(RelativeProjectPathManager.getRealFilePathToSave( directoryPathToSave + '/'+aFileName),'w') as wFile:
        wFile.write(json.dumps((ClassweekHttpRequester.getAPICallLogListGivenSessionId( aSessionId, captureDatetime))))


if __name__ == "__main__":
    startDateString = '2014-05-26'
    endDateString='2014-06-01'
    captureDatetime='2014-06-02 23:59:59'
    #
    # saveUserLog('09FN8+0qQscHPgeR5RrTmg==', 'curiosUserLog')
    # saveUserLog('c5vZhTq3BBgQeRS+S4MZFA==', 'filterUserLog')
    # saveUserLog('/2rzhbp7QK6j5ZeaNJ91Vw==', 'indifferenceUserLog')
    # saveUserLog('u36ZPhbKkBuucfTgrRv0RQ==', 'interestedUserLog')
    # saveUserLog('6xCPnJszbCVLRq5BckcXfQ==', 'paymentUserLog')
    #
    #



















