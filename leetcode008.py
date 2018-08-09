class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ls = len(str)
        if ls == 0:
            return 0
        i = 0
        res = 0
        t = 1
        while i < ls and str[i] == ' ':
            i = i + 1
        if i<ls and (str[i] == '-' or str[i] == '+'):
            if str[i] == '-':
                t = -1
            elif str[i] == '+':
                t = 1
            i = i + 1
        while i < ls and ord(str[i])>=ord('0') and ord(str[i])<=ord('9'):
            res = res * 10 + (ord(str[i]) - ord('0'))
            i = i + 1
        res = res * t
        if res > 2**31-1:
            return 2**31-1
        if res < -2**31:
            return -2**31
        return res

if __name__=="__main__":
    s = Solution()
    print(s.myAtoi(' '))
