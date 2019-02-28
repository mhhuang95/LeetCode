class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        tmp = []
        while n not in tmp:
            tmp.append(n)
            res = 0
            while n > 0:
                n,re = divmod(n,10)
                res += re**2
            n = res
        if n == 1:
            return True
        else:
            return False

