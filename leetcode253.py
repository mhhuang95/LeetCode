# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = []
        ends = []
        for x in intervals:
            starts.append(x.start)
            ends.append(x.end)

        starts.sort()
        ends.sort()
        s,e = 0,0
        res = avail = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if avail == 0:
                    res += 1
                else:
                    avail -= 1
            else:
                avail+=1
                e+=1
        return res