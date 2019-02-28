class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s.strip().split()
        for i in range(len(res)//2):
            res[i], res[len(res)-i-1] = res[len(res)-i-1],res[i]
        return " ".join(res)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("   a   b "))