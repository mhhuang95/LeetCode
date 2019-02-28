class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        ls = len(nums)
        if ls == 0:
            return res

        self.get_permute(res, nums, 0)

        return res

    def get_permute(self, res, nums, index):
        if index == len(nums):
            res.append(list(nums))
            return
        appeared = set()
        for i in range(index, len(nums)):
            if nums[i] in appeared:
                continue
            appeared.add(nums[i])
            nums[i], nums[index] = nums[index], nums[i]
            self.get_permute(res, nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 3]))