class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']
        res = []
        t = self.generateParenthesis(n-1)
        for x in t:
            h = '(' + x
            for i in range(len(h)):
                if h[i] == '(':
                    res.append(h[:i+1]+')'+h[i+1:])
        res = set(res)
        res = list(res)
        return res