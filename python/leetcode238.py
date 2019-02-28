class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [1]
        for i in range(len(nums) - 1):
            arr.append(arr[-1]*nums[i])
        temp = 1
        for j in range(len(nums) - 1,-1,-1):
            arr[j] *= temp
            temp *= nums[j]
        return arr