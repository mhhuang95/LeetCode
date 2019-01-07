class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        citations.sort(reverse = True)
        i=0
        while i < len(citations) and citations[i] > i:
            i+=1
        return i