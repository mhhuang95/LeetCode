class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for x in updates:
            res[x[0]] += x[2]
            if x[1]+1 < length:
                res[x[1]+1] -= x[2]
        curr = 0
        for i in range(length):
            curr += res[i]
            res[i] = curr
        return res