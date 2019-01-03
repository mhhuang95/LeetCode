class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [0] * (target+1)
        for i in range(1, target+1):
            for c in nums:
                if c > i:break
                if c == i:dp[i]+=1
                if c < i: dp[i]+=dp[i-c]
        return dp[target]