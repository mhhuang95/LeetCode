class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if s[i-len(w)+1:i+1]==w and (dp[i-len(w)]==True or i-len(w) == -1):
                    dp[i] = True
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode",["leet", "code"]))