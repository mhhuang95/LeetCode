class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        ls = len(nums)
        i = 0
        while i < ls-1:
            if nums[i] == nums[i+1]:
                k += 1
                if k == 3:
                    nums.pop(i+1)
                    ls = ls - 1
                    k = k -1
                    continue

                i += 1
            else:
                k = 1
                i = i + 1
        return len(nums)

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,2,3]))