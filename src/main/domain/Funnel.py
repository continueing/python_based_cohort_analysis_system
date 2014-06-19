from src.main.domain.UserBehavior import UserBehavior

__author__ = 'continueing'

class Funnel():
    def __init__(self, anUserBehaviorList):
        self.userBehaviorList = anUserBehaviorList

    def countNumberOfIndifference(self):
        return self.countNumberOfGivenType(UserBehavior.TYPE_INDIFFERENCE)

    def countNumberOfCurios(self):
        return self.countNumberOfGivenType(UserBehavior.TYPE_CURIOUS)

    def countNumberOfInterested(self):
        return self.countNumberOfGivenType(UserBehavior.TYPE_INTERESTED)

    def countNumberOfFilter(self):
        return self.countNumberOfGivenType(UserBehavior.TYPE_FILTER)

    def countNumberOfPayment(self):
        return self.countNumberOfGivenType(UserBehavior.TYPE_PAYMENT)

    def countNumberOfGivenType(self, aType):
        result = 0
        for userBehavior in self.userBehaviorList:
            if userBehavior.type == aType:
                result += 1
        return result

    # is this needed?
    def printPaymentUserSessions(self):
        print('payment users session list ')
        self.printGivenUserTypeSessions(UserBehavior.TYPE_PAYMENT)

    def printCuriosUserSessions(self):
        print('curios users session list ')
        self.printGivenUserTypeSessions(UserBehavior.TYPE_CURIOUS)

    def printInterestedUserSessions(self):
        print('interested users session list ')
        self.printGivenUserTypeSessions(UserBehavior.TYPE_INTERESTED)

    def printIndifferenceUserSessions(self):
        print('indifference users session list ')
        self.printGivenUserTypeSessions(UserBehavior.TYPE_INDIFFERENCE)

    def printFilterUserSessions(self):
        print('filter users session list ')
        self.printGivenUserTypeSessions(UserBehavior.TYPE_FILTER)

    def printGivenUserTypeSessions(self, aType):
        for userBehavior in self.userBehaviorList:
            if userBehavior.type == aType:
                print(' ' + userBehavior.sessionId)

    def __eq__(self, other):
        pass
