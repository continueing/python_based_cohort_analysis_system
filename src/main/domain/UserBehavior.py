from datetime import datetime

from src.main.domain.APICall import APICall
from src.main.network_communication.ClassweekHttpRequester import ClassweekHttpRequester


__author__ = 'continueing'


class UserBehavior():
    TYPE_INDIFFERENCE=0
    TYPE_CURIOUS = 1
    TYPE_INTERESTED = 2
    TYPE_FILTER=3
    TYPE_PAYMENT = 4

    @staticmethod
    def instantiateBasedOnSessionIdWithCaptureDatetime(aSessionId, aCaptureDatetime):
        return UserBehavior(aSessionId, ClassweekHttpRequester.getAPICallLogListGivenSessionId(aSessionId, aCaptureDatetime))


    def __init__(self, aSessionId, anAPICallList):
        self.sessionId = aSessionId
        self.apiCallList = self.makeAPICallObjectList(anAPICallList)
        self.type = self.determineType()


    def determineType(self):
        result = UserBehavior.TYPE_INDIFFERENCE
        if( self.checkIsCurious() == True):
            result = UserBehavior.TYPE_CURIOUS
        if(self.checkIsInterested() == True):
            result = UserBehavior.TYPE_INTERESTED
        if(self.checkIsFilter() == True):
            result = UserBehavior.TYPE_FILTER
        if( self.checkIsPayment() == True):
            result = UserBehavior.TYPE_PAYMENT
        return result

    def makeAPICallObjectList(self, aList):
        result =[]
        for aDict in aList:
            result.append( APICall.fromDict(aDict) )
        result.reverse()
        return result


    def printLog(self):
        print("session id : " + self.sessionId)
        for apiLogsTuple in enumerate(self.apiCallList):
            print(apiLogsTuple[0])
            print(apiLogsTuple[1])
            print ('')
        print("-" * 20)


    def isAndroidUser(self):
        if(self.apiCallList.__len__() < 2):
            return False
        for apiCall in self.apiCallList:
            if(apiCall.type == APICall.TYPE_RECOMMENDATION_CLASSES or apiCall.type == APICall.TYPE_RECOMMENDATION_SUBCATEGORY or apiCall.type == APICall.TYPE_PROMOTION ):
                return True
        return False


    def userTypeAsString(self):
        if(UserBehavior.TYPE_PAYMENT == self.type):
            return 'payment'
        if(UserBehavior.TYPE_FILTER == self.type ):
            return 'filter'
        if(UserBehavior.TYPE_CURIOUS == self.type):
            return 'curious'
        if(UserBehavior.TYPE_INTERESTED == self.type):
            return 'interested'
        else:
            return 'indifference'


    def checkIsPayment(self):
        for apiCall in self.apiCallList:
            if(apiCall.type == APICall.TYPE_PAYMENT):
                return True
        return False

    def checkIsInterested(self):
        for apiCallTuple in enumerate(self.apiCallList):
            if(apiCallTuple[1].type == APICall.TYPE_DETAIL_VIEW):
                if(self.apiCallList[apiCallTuple[0]-1].checkClassSummarySearch()):
                    return True
        pass

    def checkIsCurious(self):
        for apiCallTuple in enumerate(self.apiCallList):
            if(apiCallTuple[1].type  == APICall.TYPE_SHALLOW_SEARCH):
                    return True
            if(apiCallTuple[1].type == APICall.TYPE_DETAIL_VIEW):
                if(self.apiCallList[apiCallTuple[0]-1].checkClassSummarySearch() is False):
                    return True
        return False

    def checkIsFilter(self):
        for apiCall in self.apiCallList:
            if(apiCall.type == APICall.TYPE_FILTER):
                return True
        return False



