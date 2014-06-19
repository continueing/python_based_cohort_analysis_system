from src.main.domain.Group import Group
from src.main.domain.Snapshot import Snapshot
from src.main.domain.UserBehavior import UserBehavior
from src.main.util.TimeFormatter import TimeFormatter

__author__ = 'continueing'




if __name__ == "__main__":
    group = Group(anId=1, aStartDate=TimeFormatter.toDatetime('2014-06-15 00:00:00'), anEndDate=TimeFormatter.toDatetime('2014-06-19 23:59:59'), aNickname="6월 12일 하루")
    group.save()
    snapshot = Snapshot(group)
    snapshot.capture(TimeFormatter.toDatetime( '2014-06-20 00:00:00') )
    funnel = snapshot.funnel

    print('Indifference:\t\t' + str(funnel.countNumberOfIndifference()))
    print('curios:\t\t' + str(funnel.countNumberOfCurios()))
    print('interested:\t\t' + str(funnel.countNumberOfInterested()))
    print('filter:\t\t' + str(funnel.countNumberOfFilter()))
    print('payment:\t\t' + str(funnel.countNumberOfPayment()))


    userbehavior = UserBehavior.instantiateBasedOnSessionIdWithCaptureDatetime("09FN8+0qQscHPgeR5RrTmg==",TimeFormatter.toDatetime( '2014-06-20 00:00:00'))
    userbehavior.printLog()




