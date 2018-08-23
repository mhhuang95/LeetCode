class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        ls = len(nums)
        nums.sort()
        i = 0
        k = 1
        while i < ls:
            if nums[i]<=0:
                i = i + 1
            elif nums[i] > k:
                return k
            elif nums[i] == k:
                k = k + 1
                i = i + 1
            elif i >=1 and nums[i] == nums[i-1]:
                i = i + 1
        return k

if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1,1]))
