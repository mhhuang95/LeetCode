class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {')':'(', '}':'{', ']':'['}
        ls = len(s)
        a = []
        i = 0
        while i < ls:
            if s[i] in ['(', '{', '[']:
                a.append(s[i])
            elif len(a) > 0 and map[s[i]] == a[-1]:
                a.pop()
            else:
                return False
            i = i + 1
        if len(a) == 0:
            return True
        else:
            return False

