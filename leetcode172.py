class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeros = 0
        while n >0:
            n = n // 5
            zeros+=n
        return zeros

if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(30))