class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        i,j = 0,0
        while i < len(v1) and j < len(v2):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            i += 1
            j += 1
        if i < len(v1) and int(''.join(v1[i:]))>0:
            return 1
        elif j < len(v2) and int(''.join(v2[j:]))>0:
            return -1
        else:
            return 0