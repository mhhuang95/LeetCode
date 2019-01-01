class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = len(nums)
        if ls == 0:
            return 0
        if ls == 1:
            return nums[0]
        elif ls == 2:
            return max(nums[0], nums[1])
        elif ls == 3:
            return max(nums[1], nums[0] + nums[2])
        dp = [0] * ls
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[1], nums[0] + nums[2])

        for i in range(3, ls):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[ls - 1]

if __name__ == "__main__":
    s = Solution()
    print (s.rob([2,7,9,3,1]))