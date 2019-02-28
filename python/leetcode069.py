class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 4:
            return 1
        res = 2*self.mySqrt(x//4)
        if (res+1)*(res+1) <= x and (res+1)*(res+1) >=0:
            res = res + 1
        return res