class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        ls = len(word)
        la = len(abbr)
        i,j=0,0
        while i < ls and j < la:
            if  abbr[j] == word[i]:
                j+=1
                i+=1
            elif abbr[j] == '0':
                return False
            elif ord(abbr[j]) >= ord('0') and ord(abbr[j])<= ord('9'):
                k = j
                while j < len(abbr) and ord(abbr[j]) >= ord('0') and ord(abbr[j])<= ord('9'):
                    j += 1
                l = int(abbr[k:j])
                i += l
            else:
                return False
        if i == ls and j == la:
            return True
        else:
            return False