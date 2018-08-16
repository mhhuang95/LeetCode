class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls = len(nums)
        if ls == 1 and nums[0]==target:
            return [0,0]
        i = 0
        k = ls-1
        while i <= k:
            mid = (i + k) // 2
            if nums[mid] == target:
                l = r = mid
                while l > 0 and nums[l-1] == nums[l]:
                    l = l - 1
                while r < ls-1 and nums[r+1] == nums[r]:
                    r = r + 1
                return [l,r]
            elif nums[mid] > target:
                k = mid-1
            else:
                i = mid+1
        return [-1,-1]

if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([1,1,2],1))