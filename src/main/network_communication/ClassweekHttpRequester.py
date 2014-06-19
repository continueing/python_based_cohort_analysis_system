import http.client, urllib.parse, json
from src.main.util.TimeFormatter import TimeFormatter

__author__ = 'continueing'



class ClassweekHttpRequester():
    #BASE
    IP_ADDRESS = '175.126.82.184'
    COMMON_HEADERS = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    #POST REQUEST
    POST_STRING = "POST"
    ENCODING = "utf-8"
    URL_SESSION_IDS_GIVEN_PERIOD = '/analysis/created'
    URL_API_CALL_LOG_LIST_GIVEN_SESSION_ID = "/analysis/trace"
    POST_PARM_START_DATE = 'start_date'
    POST_PARM_END_DATE = 'end_date'
    POST_PARM_SESSION_ID = 'session_id'
    POST_PARM_CAPTURE_DATETIME = 'end_datetime'

    #RESPONSE
    SUCCESSFUL_RESULT_DATA_PARSING_KEY = 'data'

    @staticmethod
    def getSessionIdsGivenPeriod(aPeriod):
        post_params = { ClassweekHttpRequester.POST_PARM_START_DATE : TimeFormatter.toDateString(aPeriod.start)  , ClassweekHttpRequester.POST_PARM_END_DATE : TimeFormatter.toDateString(aPeriod.end)}
        response = ClassweekHttpRequester.postForDictResponse(ClassweekHttpRequester.URL_SESSION_IDS_GIVEN_PERIOD, post_params)
        return response[ClassweekHttpRequester.SUCCESSFUL_RESULT_DATA_PARSING_KEY]

    @staticmethod
    def getAPICallLogListGivenSessionId(aSessionId, aCaptureDatetime):
        response = ClassweekHttpRequester.postForDictResponse(ClassweekHttpRequester.URL_API_CALL_LOG_LIST_GIVEN_SESSION_ID, { ClassweekHttpRequester.POST_PARM_SESSION_ID : aSessionId, ClassweekHttpRequester.POST_PARM_CAPTURE_DATETIME : TimeFormatter.toDatetimeString(aCaptureDatetime)})
        return response[ClassweekHttpRequester.SUCCESSFUL_RESULT_DATA_PARSING_KEY]

    @staticmethod
    def postForDictResponse(anUrl, aParm):
        conn = http.client.HTTPConnection(ClassweekHttpRequester.IP_ADDRESS)
        conn.request(ClassweekHttpRequester.POST_STRING, anUrl, urllib.parse.urlencode(aParm), ClassweekHttpRequester.COMMON_HEADERS)
        return json.loads( conn.getresponse().read().decode(ClassweekHttpRequester.ENCODING) )


