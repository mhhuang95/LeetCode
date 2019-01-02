class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same = 0
        diff = k
        for i in range(1,n):
            tmp = diff
            diff = (same+diff)*(k-1)
            same = tmp
        return same+diff

if __name__ == "__main__":
    s = Solution()
    print(s.numWays(3,2))