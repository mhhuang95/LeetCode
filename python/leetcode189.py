class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        k = k % len(nums)
        nums = nums[-k:] + nums[:ls-k]
        return nums

        ls = len(nums)
        k = k % len(nums)
        def rotate_one(nums):
            l = nums.pop()
            nums.insert(0,l)
            return nums

        for i in range(k):
            nums = rotate_one(nums)




if __name__ == "__main__":
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7],3))