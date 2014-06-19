from unittest.case import TestCase
from src.main.domain.Funnel import Funnel
from src.main.domain.Group import Group
from src.main.domain.UserBehavior import UserBehavior

__author__ = 'continueing'



class FunnelTest(TestCase):
    numOfCurious = 5
    numOfInterested = 11
    numOfIndifference = 20
    numOfFilter = 39999
    numOfPayment = 20000

    def createUserBehavior(self, aNum, aType):
        userBehaviors = []
        for i in range(aNum):
            userBehavior = UserBehavior('',[])
            userBehavior.type = aType
            userBehaviors.append(userBehavior)
        return userBehaviors

    def setUp(self):
        userBehaviors = []
        userBehaviors = userBehaviors + self.createUserBehavior(self.numOfCurious, UserBehavior.TYPE_CURIOUS)
        userBehaviors = userBehaviors + self.createUserBehavior(self.numOfInterested, UserBehavior.TYPE_INTERESTED)
        userBehaviors = userBehaviors + self.createUserBehavior(self.numOfIndifference, UserBehavior.TYPE_INDIFFERENCE)
        userBehaviors = userBehaviors + self.createUserBehavior(self.numOfFilter, UserBehavior.TYPE_FILTER)
        userBehaviors = userBehaviors + self.createUserBehavior(self.numOfPayment, UserBehavior.TYPE_PAYMENT)
        self.funnel = Funnel(userBehaviors)

    def testCountCurious(self):
        self.assertEqual(self.funnel.countNumberOfCurios(), self.numOfCurious)
        self.assertEqual(self.funnel.countNumberOfInterested(), self.numOfInterested)
        self.assertEqual(self.funnel.countNumberOfIndifference(), self.numOfIndifference)
        self.assertEqual(self.funnel.countNumberOfFilter(), self.numOfFilter)
        self.assertEqual(self.funnel.countNumberOfPayment(), self.numOfPayment)
