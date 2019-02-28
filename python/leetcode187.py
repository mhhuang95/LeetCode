class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        for i in range(len(s)-9):
            d[s[i:i+10]] = d.get(s[i:i+10],0)+1
        return [key for key in d if d[key] >1]