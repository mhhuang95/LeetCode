class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n == 0:
            return 1
        curr = abs(n)
        while curr > 0:
            if curr & 1 == 1:
                res = res*x
            curr = curr //2
            x *= x
        if n < 0:
            res = 1/res

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.0,10))