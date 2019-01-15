class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i, sign = 0, [1,1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i+=1
                res += sign.pop()*int(s[start:i])
                continue
            if c in '+-(':
                sign += sign[-1]*(1,-1)[c == '-']
            if c == ')':
                sign.pop()
            i+=1
        return res



if __name__ == "__main__":
    s = Solution()
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))