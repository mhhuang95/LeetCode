class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds = {}
        dt = {}
        for x in s:
            ds[x] = ds.get(x,0)+1
        for x in t:
            dt[x] = dt.get(x,0)+1
        for key in dt:
            if key not in s or dt[key] == ds[key] +1:
                return dt[key]