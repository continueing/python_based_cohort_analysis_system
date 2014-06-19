from unittest.case import TestCase
from src.main.domain.UserBehavior import UserBehavior
from src.main.util.RelativeProjectPathManager import RelativeProjectPathManager
import json
from src.main.util.TimeFormatter import TimeFormatter

__author__ = 'continueing'





class UserBehaviorTest(TestCase):
    directoryPathToSave = '/src/test/resource'

    def testDetermineUserTypeAsPayment(self):
        with open(RelativeProjectPathManager.getRealFilePathToSave( UserBehaviorTest.directoryPathToSave + '/'+'paymentUserLog'),'r') as rFile:
            self.assertEqual(UserBehavior('6xCPnJszbCVLRq5BckcXfQ==',json.loads(rFile.read())).type, UserBehavior.TYPE_PAYMENT)

    def testDetermineUserTypeAsInterested(self):
        with open(RelativeProjectPathManager.getRealFilePathToSave( UserBehaviorTest.directoryPathToSave + '/'+'interestedUserLog'),'r') as rFile:
            self.assertEqual(UserBehavior('u36ZPhbKkBuucfTgrRv0RQ==',json.loads(rFile.read())).type, UserBehavior.TYPE_INTERESTED)

    def testDetermineUserTypeAsIndifference(self):
        with open(RelativeProjectPathManager.getRealFilePathToSave( UserBehaviorTest.directoryPathToSave + '/'+'indifferenceUserLog'),'r') as rFile:
            self.assertEqual(UserBehavior('/2rzhbp7QK6j5ZeaNJ91Vw==',json.loads(rFile.read())).type, UserBehavior.TYPE_INDIFFERENCE)

    def testDetermineUserTypeAsFilter(self):
        with open(RelativeProjectPathManager.getRealFilePathToSave( UserBehaviorTest.directoryPathToSave + '/'+'filterUserLog'),'r') as rFile:
            self.assertEqual(UserBehavior('c5vZhTq3BBgQeRS+S4MZFA==',json.loads(rFile.read())).type, UserBehavior.TYPE_FILTER)

    def testDetermineUserTypeAsCurios(self):
        with open(RelativeProjectPathManager.getRealFilePathToSave( UserBehaviorTest.directoryPathToSave + '/'+'curiosUserLog'),'r') as rFile:
            self.assertEqual(UserBehavior('09FN8+0qQscHPgeR5RrTmg==',json.loads(rFile.read())).type, UserBehavior.TYPE_CURIOUS)

    def testInstantiateUserBehaviorBySessionId(self):
        try:
            userBehavior = UserBehavior.instantiateBasedOnSessionIdWithCaptureDatetime(aSessionId = 'W1A/aq3DnaO6NpBrD8gbzw==', aCaptureDatetime=TimeFormatter.toDatetime('2014-06-01 11:23:30'))
        except:
            self.fail("fail to instantiate userBehavior, this function is related with http request and json parsing tasks.")

    def testIsAndroidUser(self):
        userBehavior = UserBehavior.instantiateBasedOnSessionIdWithCaptureDatetime(aSessionId = 'W1A/aq3DnaO6NpBrD8gbzw==', aCaptureDatetime=TimeFormatter.toDatetime('2014-06-11 11:23:30'))
        self.assertTrue(userBehavior.isAndroidUser())










