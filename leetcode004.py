class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if n%2 == 1:
                return nums2[n//2]
            else:
                return (nums2[n//2]+ nums2[n//2-1])/2
        if n == 0:
            if m%2 == 1:
                return nums1[m//2]
            else:
                return (nums1[m//2]+ nums1[m//2-1])/2
        p1 = p2 = 0
        new = []
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                new.append(nums1[p1])
                p1 = p1 + 1
            else:
                new.append(nums2[p2])
                p2 = p2 + 1
            if len(new)>((m+n)//2):
                break
        if p1 < m and len(new)<=((m+n)//2):
            while p1 < m:
                new.append(nums1[p1])
                p1 = p1 + 1
                if len(new) >((m+n)//2):
                    break
        if p2 < n and len(new)<=((m+n)//2):
            while p2 < n:
                new.append(nums2[p2])
                p2 = p2 + 1
                if len(new) >((m+n)//2):
                    break
        if (m+n) %2 == 1:
            return new[(m+n)//2]
        else:
            return (new[(m+n)//2] + new[(m+n)//2 - 1])/2

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1],[2,3,4]))
