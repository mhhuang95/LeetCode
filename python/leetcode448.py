class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = [0] * (len(nums)+1)
        for x in nums:
            seen[x] += 1
        return [i for i in range(1,len(nums)+1 ) if seen[i] == 0]
