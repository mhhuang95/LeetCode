class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        ls = len(nums)
        for x in nums:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
            if dic[x] >= ls // 3 + 1 and x not in res:
                res.append(x)
        return res
