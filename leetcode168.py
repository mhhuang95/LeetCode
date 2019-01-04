class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        res = ''
        while n >0:
            n, rem = divmod(n-1,26)
            res += capitals[rem]
        return res