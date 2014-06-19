from datetime import datetime

import json
from src.main.util.TimeFormatter import TimeFormatter


__author__ = 'continueing'


class APICall():
    JSON_PARM_URL = 'path_name'
    JSON_PARM_CREATED_DATE_TIME = 'created'
    JSON_PARM_PARM = 'request_params'

    TYPE_RECOMMENDATION_CLASSES = 4
    TYPE_RECOMMENDATION_SUBCATEGORY = 5
    TYPE_PROMOTION = 6
    TYPE_SHALLOW_SEARCH = 0
    TYPE_DETAIL_VIEW = 1
    TYPE_FILTER = 2
    TYPE_PAYMENT = 3

    @staticmethod
    def fromJson(aJsonString):
        jsonDict= json.loads(aJsonString)
        return APICall(anUrl=jsonDict[APICall.JSON_PARM_URL], aCreatedDateTime=TimeFormatter.toDatetime(jsonDict[APICall.JSON_PARM_CREATED_DATE_TIME]), aParm=jsonDict[APICall.JSON_PARM_PARM].__str__())

    @staticmethod
    def fromDict(aJsonDict):
        return APICall(anUrl=aJsonDict[APICall.JSON_PARM_URL], aCreatedDateTime=TimeFormatter.toDatetime(aJsonDict[APICall.JSON_PARM_CREATED_DATE_TIME]), aParm=aJsonDict[APICall.JSON_PARM_PARM].__str__())


    def __init__(self, anUrl, aCreatedDateTime, aParm):
        self.url = anUrl;
        self.createdDateTime = aCreatedDateTime;
        self.parm = str(aParm);
        self.type = self.determineType()
        self.checkFormat()

    def checkFormat(self):
        if(isinstance( self.url, str) is not True):
            raise Exception("url should be string")
        if(isinstance( self.createdDateTime, datetime) is not True):
            raise Exception("aCreatedDateTime should be datetime")
        if(isinstance( self.parm, str) is not True):
            raise Exception("aParm should be string")

    def determineType(self):
        if(self.checkShallowSearch()):
            return APICall.TYPE_SHALLOW_SEARCH
        if(self.checkDetailView()):
            return APICall.TYPE_DETAIL_VIEW
        if(self.checkFilter()):
            return APICall.TYPE_FILTER
        if(self.checkPayment()):
            return APICall.TYPE_PAYMENT
        if(self.checkRecommendationClasses()):
            return APICall.TYPE_RECOMMENDATION_CLASSES
        if(self.checkRecommendationSubcategory()):
            return APICall.TYPE_RECOMMENDATION_SUBCATEGORY
        if(self.checkPromotion()):
            return APICall.TYPE_PROMOTION
        return None


    def typeToString(self):
        if APICall.TYPE_PAYMENT == self.type:
            return 'payment'
        if APICall.TYPE_SHALLOW_SEARCH == self.type:
            return 'shallow search'
        if APICall.TYPE_DETAIL_VIEW == self.type:
            return 'detail view'
        if APICall.TYPE_FILTER == self.type:
            return 'filter'
        if APICall.TYPE_RECOMMENDATION_CLASSES == self.type:
            return 'recommendation classes'
        if APICall.TYPE_RECOMMENDATION_SUBCATEGORY == self.type:
            return 'recommendation subcategory'
        if APICall.TYPE_PROMOTION == self.type:
            return 'promotion'
        return "None"

    def __str__(self):
        return self.url + '\n' + self.parm + '\n' + TimeFormatter.toDatetimeString(self.createdDateTime) + '\n' + self.typeToString()

    def checkRecommendationClasses(self):
        # example of url : /classes/recommend/classes
        splitUrl = str(self.url).split('/')
        return splitUrl.__len__() == 4 and splitUrl[1] == 'classes' and splitUrl[2] == 'recommend' and splitUrl[3] == 'classes'

    def checkRecommendationSubcategory(self):
        # example of url : /classes/recommend/subcategory
        splitUrl = str(self.url).split('/')
        return splitUrl.__len__() == 4 and splitUrl[1] == 'classes' and splitUrl[2] == 'recommend' and splitUrl[3] == 'subcategory'

    def checkPromotion(self):
        # example of url : /classes/promotion
        splitUrl = str(self.url).split('/')
        return splitUrl.__len__() == 3 and splitUrl[1] == 'classes' and splitUrl[2] == 'promotion'

    def checkClassSummarySearch(self):
        # example of url : /classes/dance/etc/1
        splitUrl = str(self.url).split('/')
        return ( splitUrl.__len__() == 5 and splitUrl[1] == 'classes'
                 and (splitUrl[2] == 'dance'or splitUrl[2] == 'music') )

    def checkFilter(self):
        # example of url : /classes/dance/etc/1 with filter
        # return ( self.checkClassSummarySearch() and self.parm.__len__() > 2 )
        return ( self.checkClassSummarySearch() and self.parm != "{}" )

    def checkPayment(self):
        # example of url : /foradmin/before_payment
        splitUrl = str(self.url).split('/')
        return splitUrl.__len__() == 3 and splitUrl[1] == 'foradmin' and splitUrl[2] == 'before_payment'

    def checkShallowSearch(self):
        # example of url : /classes/dance/etc/1 without parm
        return ( self.checkClassSummarySearch() and self.parm == "{}" )

    def checkDetailView(self):
        # example of url: /classes/12/13
        splitUrl = str(self.url).split('/')
        if( splitUrl.__len__() == 4 and splitUrl[1] == 'classes' ):
            try :
                int(splitUrl[2])
                int(splitUrl[3])
            except :
                return False
            return True
        else:
            return False