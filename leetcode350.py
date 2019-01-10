class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)
        i = 0
        ls = len(nums2)
        while i < ls:
            if nums2[i] in nums1:
                res.append(nums2[i])
                nums1.pop(nums1.index(nums2[i]))
                nums2.pop(i)
                ls -= 1
            else:
                i+=1
        return res