from unittest.case import TestCase
from src.main.domain.Group import Group
from src.main.domain.Snapshot import Snapshot
from src.main.util.TimeFormatter import TimeFormatter

__author__ = 'continueing'

# must consider about time contradiction such as capture time is prior to group start time?

class SnapshotTest(TestCase):


    def testEnableToCapture(self):
        group = Group(anId=1, aStartDate=TimeFormatter.toDatetime('2014-06-01 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-06-01 23:59:59'), aNickname="6월 1일")
        snapshot = Snapshot(group)

        snapshot.capture(TimeFormatter.toDatetime('2014-06-07 23:59:59'))
        self.assertTrue( snapshot.funnel is not None)

        try:
            snapshot.capture(TimeFormatter.toDatetime('2014-06-01 23:59:59'))
        except:
            return
        self.fail("this is not correct time relation, should be failed")









