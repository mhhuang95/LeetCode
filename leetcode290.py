class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in dic1 and str[i] in dic2:
                return False
            elif pattern[i] in dic1 and str[i] not in dic2:
                return False
            elif pattern[i] not in dic1 and str[i] not in dic2:
                dic1[pattern[i]] = str[i]
                dic2[str[i]] = pattern[i]
            elif dic1[pattern[i]] != str[i] or dic2[str[i]] != pattern[i]:
                return False
        return True

