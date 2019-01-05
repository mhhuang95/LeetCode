class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(ord('A'), ord('Z')+1):
            dic[chr(i)] = i - ord('A')+1
        res = 0
        for x in s:
            res = res * 26 + dic[x]
        return res