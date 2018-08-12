class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        k = 1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            k = -1
        divisor = abs(divisor)
        dividend = abs(dividend)
        res = 0
        while divisor <= dividend:
            n, nb = 1, divisor

            while dividend >= nb:
                dividend, res = dividend - nb, res + n
                n, nb = n<<1, nb<<1
        if k==1:
            return min(res, 2**31-1)
        else:
            return max(-res, -2**31)
