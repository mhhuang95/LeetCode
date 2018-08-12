class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        l = ls = len(nums)
        for i in range(ls-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                l = l-1
        return l
