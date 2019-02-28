class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = {}
        self.l = len(words)
        for i ,w in enumerate(words):
            self.dic[w] = self.dic.get(w,[])+[i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        loc1 = self.dic[word1]
        loc2 = self.dic[word2]
        res = self.l
        i = j = 0
        while i < len(loc1) and j < len(loc2):
            res = min(res, abs(loc1[i]-loc2[j]))
            if loc1[i] < loc2[j]:
                i+=1
            else:
                j+=1
        return res



        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)