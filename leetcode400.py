class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        upp = 1
        i = 0
        while n >= upp+9*10**i:
            upp += 9*10**i*(i+1)
            i += 1
        if i ==0:
            return n
        n = n-upp
        n,remainder = divmod(n,i+1)
        return int(str(10**i+n)[remainder])

if __name__ == "__main__":
    s = Solution()
    print(s.findNthDigit(100))