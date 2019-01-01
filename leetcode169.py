class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ls = len(nums)
        for x in nums:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
            if dic[x] >= ls//2+1:
                return x
