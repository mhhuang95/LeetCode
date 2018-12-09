class Solution:
    #https://leetcode.com/problems/unique-binary-search-trees/discuss/202196/Python-dict-%2B-Memoization(Recursion)-32ms-Beats-99-Very-simple
    def __init__(self):
        self.dic = {}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        elif n in self.dic:
            return self.dic[n]
        else:
            out = 0
            for i in range(n):
                out += self.numTrees(i)*self.numTrees(n-i-1)
            self.dic[n] = out
            return out