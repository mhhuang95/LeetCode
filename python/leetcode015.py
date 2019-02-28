class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ls = len(nums)
        res = []
        for i in range(ls-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i+1
            k = ls-1
            while j < k:

                if nums[i]+nums[j]+nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k = k - 1
                else:
                    j = j + 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-2,0,1,1,2]))