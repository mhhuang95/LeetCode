class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for x in nums:
            dic[x] = dic.get(x,0) + 1
            if dic[x] == 2:
                dic.pop(x)
        return list(dic.keys())[0]