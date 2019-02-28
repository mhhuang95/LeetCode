class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = s.rstrip()
        ls = len(st)
        i = ls-1
        res = 0
        while i >= 0:
            if st[i] != ' ':
                res+=1
                i = i -1
            else:
                break
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord('a '))