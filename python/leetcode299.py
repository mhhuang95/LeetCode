class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        dic1 = {}
        dic2 = {}
        ls = len(secret)
        for i in range(ls):
            if secret[i] == guess[i]:
                bull +=1
            else:
                dic1[secret[i]] = dic1.get(secret[i],0) +1
                dic2[guess[i]] = dic2.get(guess[i], 0) + 1
        for x in dic1:
            if x in dic2:
                cow += min(dic1[x], dic2[x])
        return str(bull) + "A" + str(cow) + "B"