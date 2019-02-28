class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        temp = 0
        for x in nums:
            if x == 1:
                temp += 1
                res = max(res, temp)
            else:
                temp = 0

        return res