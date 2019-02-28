class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num = x
        pal = 0
        while num > 0:
            pal = pal*10 + num%10
            num = num//10
        if pal == x:
            return True
        else:
            return False