class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        rep = []
        for i in range(len(s)):
            if s[i] in s[i+1:]:
                rep.append(s[i])
            elif s[i] not in rep:
                return i

        return -1



if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))