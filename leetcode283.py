class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        i = 0
        while i < ls:
            if nums[i] == 0:
                temp = nums.pop(i)
                nums.append(temp)
                ls-=1