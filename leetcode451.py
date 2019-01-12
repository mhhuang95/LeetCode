import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c1, c2 = collections.Counter(s), {}
        for k,v in c1.items():
            c2.setdefault(v,[]).append(k*v)
        return ''.join([''.join(c2[i]) for i in range(len(s)) if i in c2])