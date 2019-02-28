class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        ls = len(s)
        res = ""
        for i in range(ls):
            j = i + 1
            k = i - 1
            while j < ls and k >= 0:
                if s[j] == s[k]:
                    j = j + 1
                    k = k - 1
                else:
                    break
            if j-k-1 > l:
                l = j-k-1
                res = s[k+1:j]
            if i + 1 < ls and s[i] == s[i+1]:
                j = i + 2
                k = i - 1
                while j < ls and k >= 0:
                    if s[j] == s[k]:
                        j = j + 1
                        k = k - 1
                    else:
                        break
                if j - k - 1 > l:
                    l = j - k - 1
                    res = s[k + 1:j]
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('ccc'))