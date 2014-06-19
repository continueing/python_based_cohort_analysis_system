from unittest.case import TestCase
from datetime import datetime
from src.main.domain.Cohort import Cohort
from src.main.domain.Group import Group
from src.main.util.TimeFormatter import TimeFormatter

__author__ = 'continueing'


class CohortTest(TestCase):

    def testAnalyzeNewGroups(self):
        cohort = Cohort(aStartDate=TimeFormatter.toDatetime('2014-05-05 00:00:00'), aEndDate=TimeFormatter.toDatetime('2014-06-01 23:59:59'), aInterval = 7)
        groups = cohort.groups

        group = Group(anId=1, aStartDate=TimeFormatter.toDatetime('2014-05-05 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-05-11 23:59:59'), aNickname="5월 1째 주")
        self.assertEqual(groups[0].period, group.period)
        group = Group(anId=2, aStartDate=TimeFormatter.toDatetime('2014-05-12 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-05-18 23:59:59'), aNickname="5월 2째 주")
        self.assertEqual(groups[1].period, group.period)
        group = Group(anId=3, aStartDate=TimeFormatter.toDatetime('2014-05-19 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-05-25 23:59:59'), aNickname="5월 3째 주")
        self.assertEqual(groups[2].period, group.period)
        group = Group(anId=3, aStartDate=TimeFormatter.toDatetime('2014-05-26 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-06-01 23:59:59'), aNickname="5월 4째 주")
        self.assertEqual(groups[3].period, group.period)
        self.assertEqual(groups.__len__(),4)

    def testSnapshots(self):
        self.fail("should test this! but take too long network time")
