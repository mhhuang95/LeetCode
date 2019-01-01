class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ls = len(words)
        res = ls
        if word2==word1:
            i = words.index(word1)
            for j in range(i+1,ls):
                if words[j] == word1:
                    res = min(res,abs(j-i))
                    i = j
        else:
            k = words.index(word1)
            j = words.index(word2)
            res = abs(k - j)
            for i in range(min(k, j) + 1, ls):
                if words[i] == word1:
                    k = i
                    res = min(res, abs(k - j))
                if words[i] == word2:
                    j = i
                    res = min(res, abs(k - j))
        return res
