class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        ls = len(s)
        for i in range(ls):

            if i > 0  and table[s[i]] > table[s[i-1]]:
                res = res + table[s[i]] - 2*table[s[i-1]]
            else:
                res = res + table[s[i]]
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt('IV'))