class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = len(nums)
        if ls == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return ls-1
        for i in range(1,ls-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i