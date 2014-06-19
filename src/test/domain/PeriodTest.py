from unittest.case import TestCase
from src.main.domain.Period import Period
from src.main.util.TimeFormatter import TimeFormatter

__author__ = 'continueing'




class PeriodTest(TestCase):

    def testContradictoryCreation(self):
        try:
            Period( TimeFormatter.toDatetime('2014-01-01 00:00:00'), TimeFormatter.toDatetime('2013-12-01 23:59:59'))
        except:
            return
        self.fail()





