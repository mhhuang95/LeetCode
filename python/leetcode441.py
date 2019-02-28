class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        k = 1
        while i+k <= n:
            i +=k
            k+=1
        return k-1

        #return int((8*n+1)**0.5-1)/2)