class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ls = len(prices)
        if ls == 0:
            return 0
        i = 1
        profit = 0
        local_min = max(prices)
        local_max = 0
        while i < ls:
            if prices[i - 1] >= prices[i]:
                i += 1
                continue
            local_min = prices[i - 1]
            while i < ls and prices[i - 1] < prices[i]:
                i += 1
            local_max = prices[i - 1]
            profit += local_max - local_min

        return profit