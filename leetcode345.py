class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ls = len(s)
        idx = []
        for i in range(ls):
            if s[i] in vowels:
                idx.append(i)
        for j in range(len(idx) // 2):
            s[idx[j]], s[idx[len(idx) - j - 1]] = s[idx[len(idx) - j - 1]], s[idx[j]]
        return ''.join(s)
