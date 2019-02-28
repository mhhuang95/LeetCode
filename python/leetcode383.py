class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for x in ransomNote:
            if x in magazine:
                magazine.pop(magazine.index(x))
            else:
                return False
        return True