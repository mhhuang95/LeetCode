class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {}
        for i in range(256):
            charMap[i] = -1
        ls = len(s)
        i = 0
        max_len = 0
        for j in range(ls):

            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            max_len = max(mex_len, j-i+1)
        return max_len



if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(''))