class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        ls = len(s)
        pre = []
        data = [0]*ls
        for i in range(ls):
            if s[i] == '(':
                pre.append(i)
            else:
                if len(pre) > 0:
                    data[i] = 1
                    data[pre.pop()] = 1
        t = 0
        for i in data:
            if i == 1:
                t = t+1
            else:
                res = max(res,t)
                t = 0
        return max(t, res)


if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses(")(((((()())()()))()(()))("))