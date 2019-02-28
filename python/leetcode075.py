class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        for i in range(ls-1, -1, -1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j + 1] = nums[j+1], nums[j]
        return