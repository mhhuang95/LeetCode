class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ls = len(prices)
        max_profit = 0
        i = 0
        while i < ls-1:
            if prices[i]>prices[i+1]:
                i += 1
                continue
            for j in range(i+1,ls):
                if prices[j] > prices[i]:
                    max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit

'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(prices==[]):
            return 0;
        x=prices[0];
        temp=0;
        for i in prices:
            if(x>i):
                x=i;
            if(temp<i-x):
                temp=i-x;
        return temp;
                
            '''