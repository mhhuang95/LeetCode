class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for x in nums:
            if x in dic:
                return True
            else:
                dic[x] = 1
                
        return False