class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        ls = len(s)
        lt = len(t)
        if ls > lt:
            return self.isOneEditDistance(t,s)
        if lt - ls > 1:
            return False
        if lt == ls:
            i = 0
            while i < ls:
                if s[i] != t[i]:
                    if s[i + 1:] == t[i + 1:]:
                        return True
                    else:
                        return False
                i += 1
        if lt == ls + 1:
            if ls == 0:
                return True
            i = 0
            while i < ls:
                if s[i] != t[i]:
                    if s[i:] == t[i + 1:]:
                        return True
                    else:
                        return False
                i += 1
            return True
        else:
            return False