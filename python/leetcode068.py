class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        ls = len(words)
        l = -1
        p = []
        while ls > 0:
            ls -= 1
            word = words.pop(0)
            l += len(word)+1
            if l > maxWidth:
                res.append(self.justify(p, maxWidth))
                p = []
                p.append(word)
                l = len(word)
            else:
                p.append(word)
        if p != None:
            t = ' '.join(p)
            res.append(t + ' '*(maxWidth-len(t)))
        return res

    def justify(self, p, maxWidth):
        ls = len(p)
        if ls == 1:
            return p[0]+' '*(maxWidth-len(p[0]))
        res = ''
        l = 0
        for i in range(ls):
            l += len(p[i])
        space = []
        x, y = divmod(maxWidth - l, ls-1)
        for i in range(y):
            space.append(x+1)
        for i in range(y,ls-1):
            space.append(x)
        for i in range(ls-1):
            res = res + p[i] + ' '*space[i]
        res = res + p[ls-1]
        return res

if __name__ == "__main__":
    s =Solution()
    print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))
