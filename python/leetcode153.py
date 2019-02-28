class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[-1]>nums[0]:
            return nums[0]
        ls = len(nums)
        i = ls-1
        while nums[i]>nums[i-1]:
            i-=1
        return nums[i]



class Solution(object):
    def findMin(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        start, end = 0, len(nums) - 1
        if nums[start] < nums[end]:
                return nums[start]
            
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[start] < nums[end]:
                return nums[start]
            if nums[start] < nums[mid]:
                start = mid
            else:
                end = mid 
                
        return nums[end]