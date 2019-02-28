class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i**2 < num:
            i+=1
        if i**2 == num:
            return True
        else:return False