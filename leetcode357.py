class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        dp = [0]*(n+1)
        dp[1] = 10
        temp = 9
        for i in range(2, n+1):
            if i > 10:
                temp = 0
            if i == 2:
                temp = temp **2
            if 2 < i :
                temp = temp*(11-i)
            dp[i] = dp[i-1] + temp
        return dp[n]
