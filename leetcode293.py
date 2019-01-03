class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ls = len(s)

        res = []
        for i in range(1,ls):
            if s[i] == s[i-1] and s[i] == "+":
                res.append(s[0:i-1]+'--'+s[i+1:] )
        return res