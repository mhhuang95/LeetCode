class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for v,x in enumerate(nums):
            if x in dic and v-dic[x] <= k:
                return True
            else:
                dic[x] = v
        return False