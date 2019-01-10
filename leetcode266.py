class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for x in s:
            dic[x] = dic.get(x,0)+1
        t = 0
        for key in dic:
            if dic[key] % 2 == 1:
                t+=1
        if t >1:
            return False
        else:
            return True