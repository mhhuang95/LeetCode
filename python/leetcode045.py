class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #ls = len(nums)
        #if ls == 1:
        #    return 0
        #dp = [0 for _ in range(ls)]
        #for i in range(ls-1, -1, -1):
        #    if i < ls-1 and dp[i] == 0:
        #        continue
        #    for j in range(i-1, -1, -1):
        #        if i-j <= nums[j] and (dp[j] == 0 or dp[i]+1 < dp[j]):
        #            dp[j] = dp[i] + 1

        #return dp[0]

        if len(nums) <= 1:
            return 0
        ls = len(nums)
        start = 0
        end = 0 + nums[0]
        step = 1
        maxdis = 0+nums[0]
        while end < ls - 1:
            for i in range(start+1,end+1):
                maxdis = max(maxdis, nums[i]+i)
            start = end
            end = maxdis
            step += 1
        return step




if __name__ == "__main__":
    s = Solution()
    print(s.jump())

