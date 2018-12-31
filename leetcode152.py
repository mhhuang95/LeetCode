class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #https: // leetcode.com / problems / maximum - product - subarray / discuss / 210384 / Python - DP - Time - O(N) - Space - O(1)

        promax = promin = res = nums[0]
        for num in nums[1:]:
            if num < 0:
                promax, promin = promin, promax

            promax = max(num, num*promax)
            promin = min(num, num*promin)
            res = max(res, promax)
        return res