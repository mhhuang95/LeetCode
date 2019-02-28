class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ls = len(words)
        res = []
        if ls == 0:
            return res
        l = len(words[0])
        total_l = l*ls
        for i in range(len(s)-total_l+1):
            x = words.copy()
            hey = s[i:i+total_l]
            for j in range(ls):
                if hey[j*l:j*l+l] in x:
                    x.pop(x.index(hey[j*l:j*l+l]))
                else:
                    break
            if len(x)==0:
                res.append(i)
        return res


