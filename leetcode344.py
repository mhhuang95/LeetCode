class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        ls = len(s)
        start = 0
        end = ls-1
        while start < end:
            s[start], s[end] = s[end],s[start]
            start+=1
            end-=1
        return ''.join(s)