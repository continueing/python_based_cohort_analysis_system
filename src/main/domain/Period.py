import copy
from datetime import datetime

__author__ = 'continueing'


class Period:
    INDEX_YEAR = 0
    INDEX_MONTH = 1
    INDEX_DAY = 2

    def __init__(self, aStart, anEnd):
        self.start = aStart
        self.end = anEnd
        if self.start > self.end:
            raise Exception("end is prior to start")

    def start(self):
        return copy.deepcopy(self.start)

    def end(self):
        return copy.deepcopy(self.end)

    def __eq__(self, other):
        if(self.start != other.start):
            return False
        if(self.end != other.end):
            return False
        return True