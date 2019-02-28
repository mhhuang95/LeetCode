class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        ls = len(s)
        dp = [0] * (ls+1)
        dp[0] = 1
        dp[1] = 1
        i = 1
        set1 = ['1', '2']

        while i < ls:
            if s[i] == '0':
                if s[i-1] not in ['1', '2']:
                    return 0
                dp[i+1] = dp[i-1]
            elif s[i - 1] == '1' or (s[i-1] == '2' and int(s[i])<7):
                dp[i+1] = dp[i]+dp[i-1]
            else:
                dp[i+1] = dp[i]
            i += 1
        return dp[ls]

