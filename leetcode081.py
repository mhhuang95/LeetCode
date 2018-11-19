class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        ls = len(nums)
        if ls == 0:
            return False
        if nums[0] > target:
            for i in range(ls-1,-1,-1):
                if nums[i] == target:
                    return True
        else:
            for i in range(ls):
                if nums[i] == target:
                    return True
        return False