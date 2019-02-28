class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ls = len(needle)
        l = len(haystack)
        if ls == 0:
            return 0
        for i in range(l-ls+1):
            if haystack[i:i+ls]==needle:
                return i
        return -1
