class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)

        diff = []
        for i in range(1, len(nums)):
            x = nums[i] - nums[i-1]
            if x != 0:
                diff.append(x)

        if len(diff) == 0:
            return 1

        count = 1
        for i in range(1, len(diff)):
            prod = diff[i]*diff[i-1]
            if prod < 0:
                count += 1
        return count + 1