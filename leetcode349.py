class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for x in set(nums1+nums2):
            if x in nums1 and x in nums2:
                res.append(x)
        res = list(set(res))
        return res