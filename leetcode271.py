class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        return ''.join("%d:" % len(s) + s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = []
        ls = len(s)
        i = 0
        while i < ls:
            j = s.find(':', i)
            l = int(s[i:j])
            res.append(s[j+1:j+1+l])
            i = j+1+l
        return res



        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(strs))