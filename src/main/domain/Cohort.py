from datetime import timedelta
from src.main.domain.Group import Group
from src.main.domain.Snapshot import Snapshot
from src.main.util.TimeFormatter import TimeFormatter

__author__ = 'continueing'


class Cohort:

    def __init__(self, aStartDate, aEndDate, aInterval):
        self.groups = []
        startDate = aStartDate
        while True:
            endDate = startDate + timedelta(days=aInterval) - timedelta(seconds=1)
            if(endDate <=  aEndDate):
                self.groups.append(Group(1, startDate , endDate, str("cohort") ))
            else:
                break
            startDate = startDate + timedelta(days=aInterval)


    def snapshots(self, aWeek):
        result = []
        for group in self.groups:
            snapshot= Snapshot(group)
            snapshot.capture(group.period.end + timedelta(days=(aWeek-1)*7 + 1))
            result.append(snapshot)
        return result



