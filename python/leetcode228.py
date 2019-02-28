class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        res = []
        low = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                high = nums[i-1]
                if low == high:
                    res.append(str(low))
                else:
                    res.append(str(low)+"->"+str(high))
                low = nums[i]

        if low < nums[-1]:
            res.append(str(low) + "->" + str(nums[-1]))
        else:
            res.append(str(low))
        return res

