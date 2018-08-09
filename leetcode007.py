class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            i = -1
            x = -x
        else:
            i = 1

        res = 0
        while x != 0:
            t = x % 10
            x = x // 10
            res = res*10 + t
        if i*res > -2**31 and i*res<2**31-1:
            return i*res
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(1463847412))