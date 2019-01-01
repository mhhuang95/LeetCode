class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1
        return [i for i in count if count[i] == 2]