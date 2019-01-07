class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        dt = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in ds and t[i] not in dt:
                ds[s[i]] = t[i]
                dt[t[i]] = s[i]
            elif s[i] in ds and t[i] in dt:
                if ds[s[i]] == t[i] and  dt[t[i]] == s[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True