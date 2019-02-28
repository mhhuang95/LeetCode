class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ls = len(nums)
        if target < nums[0]:
            return 0
        if target > nums[ls-1]:
            return ls
        i = 0
        k = ls-1
        while i <= k:

            mid = (i+k)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                k = mid
            else:
                i = mid
            if i == k - 1:
                if target > nums[i] and target <= nums[k]:
                    return k
                elif nums[i] == target:
                    return i

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3],3))
