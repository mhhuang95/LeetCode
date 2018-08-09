
        #ls = len(s)
        #lp = len(p)
        #if lp == 0 and ls>0:
        #    return False
        #if p[0] == '*':
        #    return False
        #i = j = 0
        #while i < ls and j < lp:
        #    if j+1 < lp and p[j+1] == '*':

        #        if p[j] != '.' and p[j] != s[i]:
        #            j = j + 2
        #        elif p[j]!= '.' and (j+2<lp and p[j+2]==s[i]):
        #            k = 0
        #            while j + 2 + k < lp and p[j + 2 + k] == p[j]:
        #                k = k + 1
        #            t = 1
        #            while i + t<ls and s[i + t] == s[i]:
        #                t = t + 1
        #            if k > t:
        #                return False
        #            else:
        #                j = j + k + 2
        #                i = i + t
        #        elif p[j]!= '.':
        #            t = 1
        #            while i + t < ls and s[i + t] == s[i]:
        #                t = t + 1
        #            i = i + t
        #            j = j + 2
        #        else:
        #            if j + 2 < lp and i < ls:
        #                for x in range(i, ls):
        #                    e = self.isMatch(s[x:], p[j+2:])
        #                    if e == True:
        #                        return True
        #            elif j+2 == lp:
        #                return True
        #            return False


        #    elif s[i] == p[j] or p[j] == '.':
        #        i = i + 1
        #        j = j + 1
        #    else:
        #        return False
        #if i == ls and j == lp:
        #    return True
        #else:
        #    return False

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # bottom up o(m*n)
        # https://leetcode.com/discuss/93024/easy-dp-java-solution-with-detailed-explanation
        if s == p:
            return True
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n):
            if p[j] == '*' and dp[0][j - 1]:
                dp[0][j + 1] = True
        # print dp
        for i in range(m):
            for j in range(n):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
        return dp[m][n]




if __name__== "__main__":
    s = Solution()
    print(s.isMatch("aaa","ab*a*c*a"))





