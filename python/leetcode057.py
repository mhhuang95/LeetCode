# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        intervals.sort(key = self.take_start)
        i = 0
        while i < len(intervals)-1:
            if intervals[i].end >= intervals[i+1].start:
                nexts = intervals.pop(i+1)
                if nexts.end > intervals[i].end:
                    intervals[i].end = nexts.end
            else:
                i = i + 1
        return intervals

    def take_start(self, interval):
        return interval.start