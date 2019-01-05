class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num //10 != 0:
            res = 0
            while num > 0:
                num, remainder = divmod(num,10)
                res += remainder
            num = res
        return num