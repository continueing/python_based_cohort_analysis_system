from src.main.domain.Funnel import Funnel
from src.main.domain.UserBehavior import UserBehavior

__author__ = 'continueing'



class Snapshot:

    def __init__(self, aGroup):
        self.group = aGroup
        self.funnel = None

    def capture(self, aDatetime):
        if(aDatetime <= self.group.period.end):
            raise Exception("a datetime should be later than end!")
        result = []
        for session in self.group.retrieveSessionIds():
            candidateUser = UserBehavior.instantiateBasedOnSessionIdWithCaptureDatetime(session, aDatetime)
            if(candidateUser.isAndroidUser()):
                result.append(candidateUser)
        self.funnel = Funnel(result)

