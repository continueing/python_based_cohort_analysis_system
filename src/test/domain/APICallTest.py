from unittest.case import TestCase
from src.main.domain.APICall import APICall
import json
from src.main.util.TimeFormatter import TimeFormatter


__author__ = 'continueing'



class APICallTest(TestCase):

    def testTypeDeterminationOfShallowSearch(self):
        apiCall = APICall(anUrl="/classes/dance/etc/1", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{}")
        self.assertEqual( apiCall.type, APICall.TYPE_SHALLOW_SEARCH )
        apiCall = APICall(anUrl="/classes/music/etc/2", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{}")
        self.assertEqual( apiCall.type, APICall.TYPE_SHALLOW_SEARCH )
        apiCall = APICall(anUrl="/classes/music", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{}")
        self.assertEqual( apiCall.type, None )
        apiCall = APICall(anUrl="/classes/kk/ho/123", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{}")
        self.assertEqual( apiCall.type, None )

    def testTypeDeterminationOfDetailView(self):
        apiCall = APICall(anUrl="/classes/1/3", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{}")
        self.assertEqual( apiCall.type, APICall.TYPE_DETAIL_VIEW )
        apiCall = APICall(anUrl="/classes/123123/7777", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{}")
        self.assertEqual( apiCall.type, APICall.TYPE_DETAIL_VIEW )
        apiCall = APICall(anUrl="/classes/123123/7777/123", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{}")
        self.assertEqual( apiCall.type, None )
        apiCall = APICall(anUrl="/classes/123123", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{r}")
        self.assertEqual( apiCall.type, None )

    def testTypeDeterminationOfFilter(self):
        apiCall = APICall(anUrl="/classes/dance/etc/1", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{'time':'012', 'location':'강남'}")
        self.assertEqual( apiCall.type, APICall.TYPE_FILTER )
        apiCall = APICall(anUrl="/classes/music/hoho/1", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{'time':'012'}")
        self.assertEqual( apiCall.type, APICall.TYPE_FILTER )

    def testTypeDeterminationOfPayment(self):
        apiCall = APICall(anUrl="/foradmin/before_payment", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{'time':'012', 'location':'강남'}")
        self.assertEqual( apiCall.type, APICall.TYPE_PAYMENT )
        apiCall = APICall(anUrl="/foradmin/before_payment/asd", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{'time':'012', 'location':'강남'}")
        self.assertEqual( apiCall.type, None )
        apiCall = APICall(anUrl="/foradmin", aCreatedDateTime=TimeFormatter.toDatetime("2014-02-12 23:11:20"), aParm="{'time':'012', 'location':'강남'}")
        self.assertEqual( apiCall.type, None )

    def testInstantiateFromDict(self):
        jsonDic = {}
        jsonDic[APICall.JSON_PARM_URL] = "/foradmin/before_payment"
        jsonDic[APICall.JSON_PARM_CREATED_DATE_TIME] = "2014-02-12 13:22:12"
        jsonDic[APICall.JSON_PARM_PARM] = { 'location' : 'ganngnam'}

        apiCall = APICall.fromDict(json.loads(json.dumps(jsonDic)) )
        self.assertEqual(apiCall.__str__(), jsonDic[APICall.JSON_PARM_URL] + '\n' + str(jsonDic[APICall.JSON_PARM_PARM]) + '\n' + jsonDic[APICall.JSON_PARM_CREATED_DATE_TIME] + '\n' + 'payment' )

    def testInstantiateFromJson(self):
        jsonDic = {}
        jsonDic[APICall.JSON_PARM_URL] = "/foradmin/before_payment"
        jsonDic[APICall.JSON_PARM_CREATED_DATE_TIME] = "2014-02-12 13:22:12"
        jsonDic[APICall.JSON_PARM_PARM] = { 'location' : 'ganngnam'}

        apiCall = APICall.fromJson(json.dumps(jsonDic) )
        self.assertEqual(apiCall.__str__(), jsonDic[APICall.JSON_PARM_URL] + '\n' + str(jsonDic[APICall.JSON_PARM_PARM]) + '\n' + jsonDic[APICall.JSON_PARM_CREATED_DATE_TIME] + '\n' + 'payment')















