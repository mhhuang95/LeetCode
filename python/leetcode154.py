class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0]<nums[-1]:
            return nums[0]
        ls = len(nums)
        k = 0
        for i in range(ls-1):
            if nums[i] > nums[i+1]:
                k = i+1
                break
        return nums[k]
if __name__ == "__main__":
    s = Solution()
    print(s.findMin([2,2,2,0,1]))