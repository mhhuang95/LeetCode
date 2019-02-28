class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        m,n = len(costs), len(costs[0])
        dp = [[0]*n for i in range(m)]
        dp[0] = costs[0]
        for i in range(1,m):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][1], dp[i - 1][0])
        return min(dp[-1])