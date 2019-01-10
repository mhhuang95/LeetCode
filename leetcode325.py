class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        val = 0
        dic = {0:-1}
        for i in range(len(nums)):
            val += nums[i]
            if val not in dic:
                dic[val] = i
            if val - k in dic:
                res = max(res, i - dic[val-k])
        return res