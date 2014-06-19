
from src.main.domain.Group import Group
from src.main.domain.Snapshot import Snapshot
from src.main.util.TimeFormatter import TimeFormatter

__author__ = 'continueing'


if __name__ == "__main__":
    print("indifference, curious, interested, filter, payment")
    # group = Group(anId=1, aStartDate=TimeFormatter.toDatetime('2014-05-05 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-05-11 23:59:59'), aNickname="5월 1째 주")
    # snapshot = Snapshot(group)
    # funnel = snapshot.capture(TimeFormatter.toDatetime( '2014-05-13 00:00:00') )
    # print(str(funnel.countNumberOfIndifference()) + ', ' + str(funnel.printCuriosUserSessions()) + ', ' + str(funnel.printInterestedUserSessions()) + ', ' + str(funnel.countNumberOfFilter()) + ', ' + str(funnel.countNumberOfPayment()) )

    # group = Group(anId=2, aStartDate=TimeFormatter.toDatetime('2014-05-12 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-05-18 23:59:59'), aNickname="5월 2째 주")
    # snapshot = Snapshot(group)
    # funnel = snapshot.capture(TimeFormatter.toDatetime( '2014-05-20 00:00:00') )
    # print(str(funnel.countNumberOfIndifference()) + ', ' + str(funnel.countNumberOfCurios()) + ', ' + str(funnel.countNumberOfInterested()) + ', ' + str(funnel.countNumberOfFilter()) + ', ' + str(funnel.countNumberOfPayment()) )
    #
    #
    # group = Group(anId=3, aStartDate=TimeFormatter.toDatetime('2014-05-19 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-05-25 23:59:59'), aNickname="5월 3째 주")
    # snapshot = Snapshot(group)
    # funnel = snapshot.capture(TimeFormatter.toDatetime( '2014-05-27 00:00:00') )
    # print(str(funnel.countNumberOfIndifference()) + ', ' + str(funnel.countNumberOfCurios()) + ', ' + str(funnel.countNumberOfInterested()) + ', ' + str(funnel.countNumberOfFilter()) + ', ' + str(funnel.countNumberOfPayment()) )
    #
    # group = Group(anId=3, aStartDate=TimeFormatter.toDatetime('2014-05-26 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-06-01 23:59:59'), aNickname="5월 4째 주")
    # snapshot = Snapshot(group)
    # funnel = snapshot.capture(TimeFormatter.toDatetime( '2014-06-03 00:00:00') )
    # print(str(funnel.countNumberOfIndifference()) + ', ' + str(funnel.countNumberOfCurios()) + ', ' + str(funnel.countNumberOfInterested()) + ', ' + str(funnel.countNumberOfFilter()) + ', ' + str(funnel.countNumberOfPayment()) )
    #
    # group = Group(anId=3, aStartDate=TimeFormatter.toDatetime('2014-06-02 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-06-08 23:59:59'), aNickname="6월 1째 주")
    # snapshot = Snapshot(group)
    # funnel = snapshot.capture(TimeFormatter.toDatetime( '2014-06-10 00:00:00') )
    # print(str(funnel.countNumberOfIndifference()) + ', ' + str(funnel.countNumberOfCurios()) + ', ' + str(funnel.countNumberOfInterested()) + ', ' + str(funnel.countNumberOfFilter()) + ', ' + str(funnel.countNumberOfPayment()) )

    group = Group(anId=3, aStartDate=TimeFormatter.toDatetime('2014-06-09 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-06-14 23:59:59'), aNickname="5월 4째 주")
    snapshot = Snapshot(group)
    funnel = snapshot.capture(TimeFormatter.toDatetime( '2014-06-16 00:00:00') )
    print(str(funnel.countNumberOfIndifference()) + ', ' + str(funnel.countNumberOfCurios()) + ', ' + str(funnel.countNumberOfInterested()) + ', ' + str(funnel.countNumberOfFilter()) + ', ' + str(funnel.countNumberOfPayment()) )