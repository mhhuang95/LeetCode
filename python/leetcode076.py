class Solution:
    '''
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t)>len(s):
            return ''
        doc = {}
        ls = len(s)
        min_l = 1000000000000000000
        start, end = 0,0
        l,r = 0,0
        for x in t:
            doc[x] = 0

        while r < ls:
            if s[r] in t:
                doc[s[r]] += 1
            while self.contain_t(doc):
                if r-l < min_l:
                    min_l = r - l
                    start = l
                    end = r+1
                if s[l] in t:
                    doc[s[l]] -= 1
                    if not self.contain_t(doc):
                        l = l +1
                        break

                l = l + 1

            r = r + 1

        return s[start:end]

    def contain_t(self,doc):
        for key in doc.keys():
            if doc[key] == 0:
                return False
        return True
    '''

    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))