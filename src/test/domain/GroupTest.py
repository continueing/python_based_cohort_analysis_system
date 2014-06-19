from src.main.util.RelativeProjectPathManager import RelativeProjectPathManager
from src.main.util.TimeFormatter import TimeFormatter
from unittest.case import TestCase
from src.main.domain.Group import Group

__author__ = 'continueing'

import os



class GroupTest(TestCase):
    directoryPathToSave = '/src/test/resource/group'

    def setUp(self):
        try:
            os.remove(RelativeProjectPathManager.getRealFilePathToSave(Group.FILE_PATH_TO_SAVE))
        except:
            pass
        Group.FILE_PATH_TO_SAVE = GroupTest.directoryPathToSave
        self.groups = []
        self.groups.append( Group(anId=1, aStartDate=TimeFormatter.toDatetime('2014-06-01 00:00:00') , anEndDate=TimeFormatter.toDatetime('2014-06-01 23:59:59'), aNickname="5월 4째주") )
        self.groups.append( Group(anId=2, aStartDate=TimeFormatter.toDatetime('2011-09-09 00:00:00'), anEndDate=TimeFormatter.toDatetime('2013-12-12 23:59:59'), aNickname="ㅋㅋㅋ") )


    def testGetAllWithNoFile(self):
        self.assertEqual(Group.all().__len__(), 0)

    def testCreateGroup(self):
        self.saveAll(self.groups)
        for index in enumerate(Group.all()):
            self.assertTrue( self.groups[index[0]].__eq__(index[1]), "Must be same")


    def testUpdate(self):
        self.saveAll(self.groups)
        newGroup = Group(anId=1, aStartDate=TimeFormatter.toDatetime('2013-01-01 00:00:00'), anEndDate=TimeFormatter.toDatetime('2015-12-10 23:59:59'), aNickname="2013~2015")
        newGroup.save()


    def testGetAll(self):
        self.saveAll(self.groups)
        savedGroups = Group.all()
        for newGroup in self.groups:
            self.assertTrue(newGroup.__eq__(savedGroups.pop(0)))

    def testFindById(self):
        self.saveAll(self.groups)
        self.assertEqual(self.groups[0], Group.findById(1))
        self.assertEqual(self.groups[1], Group.findById(2))

    def testCannotFindById(self):
        self.saveAll(self.groups)
        self.assertEqual(None, Group.findById(3))

    def testDelete(self):
        self.saveAll(self.groups)
        Group.delete(1)
        self.assertTrue(Group.findById(1) is None)
        self.assertTrue(Group.findById(2) is not None)
        Group.delete(2)
        self.assertTrue(Group.findById(2) is None)

    def tearDown(self):
        pass

    def saveAll(self, groups):
        for group in groups:
            group.save()



    def testRetrieveSessionIds(self):
        self.saveAll(self.groups)
        groupOne = Group.findById(1)
        userBehaviorList = groupOne.retrieveSessionIds()
        self.assertTrue( isinstance(userBehaviorList[0],str) )







