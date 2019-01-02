class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] *(num+1)
        offset = 1
        for i in range(1,num+1):
            if offset*2==i:
                offset = offset*2
            dp[i] = dp[i-offset]+1
        return dp