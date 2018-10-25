class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx, p_idx = 0,0
        star, s_star = -1, 0
        ls, lp = len(s), len(p)
        while s_idx < ls:
            if p_idx < lp and (s[s_idx] == p[p_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            elif p_idx < lp and p[p_idx] == '*':
                star = p_idx
                s_star = s_idx
                p_idx += 1
            elif star != -1:
                p_idx = star + 1
                s_star += 1
                s_idx = s_star
            else:
                return False
        while p_idx < lp and p[p_idx] == '*':
            p_idx +=1


