class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        ls = len(nums)
        nums.sort()
        for i in range(ls - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            while j < ls-2:
                while j > i+1 and j < ls -2 and nums[j] == nums[j - 1]:
                    j = j + 1
                k = j + 1
                l = ls-1
                while k < l:
                    curr = nums[i] + nums[j] + nums[k] + nums[l]
                    if curr == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k = k + 1
                        while k < l and nums[l-1] == nums[l]:
                            l = l - 1
                        k = k + 1
                        l = l - 1
                    elif curr > target:
                        l = l - 1
                    else:
                        k = k + 1
                j = j + 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([-3,-4,-5,0,-5,-2,5,2,-3],3))