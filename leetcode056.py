# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
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

def transfer(l):
    res = []
    for x in l:
        res.append(Interval(x[0], x[1]))

    return res

def back(l):
    res = []
    for x in l:
        res.append([x.start, x.end])
    return res

if __name__ == "__main__":
    s = Solution()
    print(back(s.merge(transfer([[1,4],[0,2],[3,5]]))))