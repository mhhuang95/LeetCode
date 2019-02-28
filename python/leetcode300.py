class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = len(nums)
        if ls == 0:
            return 0
        dp = [1]*ls
        for i in range(1,ls):
            dp[i] = max([0]+[dp[j] for j in range(i) if nums[i] > nums[j]])+1
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))