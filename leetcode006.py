class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s
        p = 2*numRows-2
        res = [""]*numRows
        for i in range(len(s)):
            l = i%p
            if l >= p//2:
                l = p - l
            res[l] = res[l]+s[i]
        return ''.join(res)

