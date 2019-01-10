class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        dt = {}
        for x in s:
            ds[x] = ds.get(x,0) + 1
        for x in t:
            dt[x] = dt.get(x, 0) + 1
        for key in set(list(ds.keys()) + list(dt.keys())):
            if key not in dt or dt[key]!=ds[key]:
                return False
        return True