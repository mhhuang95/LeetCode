class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n == 0:
            return m

        dp = [[None for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                cost = 0 if word1[i-1] == word2[j-1] else 1
                dp[i][j] = min(dp[i-1][j-1] + cost, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]