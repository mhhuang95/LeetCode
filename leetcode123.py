class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ls = len(prices)
        profit = 0
        i = 1
        temp = 0
        while i < ls:
            if prices[i-1]>=prices[i]:
                i += 1
                continue
            while i < ls and prices[i-1]<prices[i]:
                i += 1
            temp = max(temp, self.onetrans(prices[0:i])+self.onetrans(prices[i:]))
        return temp

    def onetrans(self,prices):
        temp = 0
        if len(prices) == 0:
            return 0
        i = prices[0]
        for x in prices:
            if x < i:
                i = x
            elif x-i>temp:
                temp = x-i
        return temp