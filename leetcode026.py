class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = len(nums)
        if ls == 0:
            return 0
        k = 0
        j = 1
        for i in range(1, ls):
            if nums[i] == nums[k]:
                continue
            else:
                nums[j] = nums[i]
                k = i
                j = j + 1
        return j



if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,2]))