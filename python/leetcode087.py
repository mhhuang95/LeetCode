class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #https://leetcode.com/problems/scramble-string/discuss/168869/Python-6-lines-short-DFS-(and-a-super-slow-DP-solution)
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if ((self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:], s2[:-i]))):
                return True
        return False