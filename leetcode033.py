class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ls = len(nums)
        if ls == 0:
            return -1
        if nums[0] >=target:
            for i in range(ls):
                if nums[i] == target:
                    return i
        else:
            for i in range(ls-1, -1, -1):
                if nums[i] == target:
                    return i
        return -1