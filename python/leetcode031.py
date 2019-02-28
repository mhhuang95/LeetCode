class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = -1
        ls = len(nums)
        for i in range(ls - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pos = i - 1
                break
        if pos == -1:
            self.re_order(nums, 0, ls - 1)
            return nums
        for i in range(ls - 1, -1, -1):
            if nums[i] > nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
                self.re_order(nums, pos + 1, ls - 1)
                break
        return nums

    def re_order(self, a, start, end):
        for i in range(0, (end - start + 1) // 2):
            a[start + i], a[end - i] = a[end - i], a[start + i]
        return a

if __name__ == "__main__":
    s = Solution()
    print(s.nextPermutation([1,3,2]))
