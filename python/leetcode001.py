class Solution():
    def twoSum(self, nums, target):
        L = sorted(nums)
        ls = len(nums)
        res = []
        i = 0
        j = ls - 1
        while i <= j:
            if L[i] + L[j] == target:
                for k, num in enumerate(nums):
                    if num == L[i] or num == L[j]:
                        res.append(k)
                return res
            elif L[i] + L[j] > target:
                j = j - 1
            elif L[i] + L[j] < target:
                i = i + 1




