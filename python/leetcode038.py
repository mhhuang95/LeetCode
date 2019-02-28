class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            s = self.countAndSay(n-1)
            ls = len(s)
            res = ''
            m = 1
            if ls == 1:
                return '11'
            for i in range(ls-1):
                if s[i+1] != s[i]:
                    res = res + str(m) + s[i]
                    m = 1
                else:
                    m = m + 1
            res = res + str(m)+s[-1]
            return res

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))