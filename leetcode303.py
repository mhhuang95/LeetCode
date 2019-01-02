class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        nums = self.nums
        if i == 0:
            return nums[j]
        return nums[j] - nums[i-1]


        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)