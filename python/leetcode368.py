class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    if len(dp[j])+1 > len(dp[i]):
                        dp[i] = list(dp[j])
                        dp[i].append(nums[i])
        for x in dp:
            if len(x) > len(res):
                res = x
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.largestDivisibleSubset([1,2,3]))