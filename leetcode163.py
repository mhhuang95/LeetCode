class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        """
        if lower == upper:
            if len(nums) == 0:
                return [str(lower)]
            else:
                return []
        if len(nums) == 0:
            return [str(lower)+'->'+str(upper)]
        res = []
        nums.insert(0,lower)
        nums.append(upper)
        ls= len(nums)
        for i in range(1,ls):
            if i == 1:
                if nums[i] - nums[i - 1] == 0:
                    continue
                elif nums[i] - nums[i-1] == 1:
                    res.append(str(lower))
                else:
                    res.append(str(lower)+"->"+str(nums[1]-1))

            elif i == ls-1:
                if nums[i] - nums[i - 1] == 0:
                    continue
                elif nums[i] - nums[i-1] == 1:
                    res.append(str(upper))
                else:
                    res.append(str(lower)+"->"+str(nums[1]-1))


                                            nums[i] - nums[i-1] == 1 or nums[i] - nums[i-1] == 0:
                continue
            elif nums[i] - nums[i-1] == 2:
                res.append(str(nums[i-1]+1))
            elif i <ls-1:
                res.append(str(nums[i-1] + 1)+'->'+str(nums[i] - 1))
            else:
                res.append(str(nums[i-1] + 1) + '->' + str(nums[i]))
        return res
        """

        res = []

        for i in range(len(nums)):
            if lower < nums[i] - 1:
                res.append(str(lower)+"->"+str(nums[i]-1))
            elif lower == nums[i] - 1:
                res.append(str(lower))
            lower = nums[i]+1

        if lower < upper:
            res.append(str(lower)+"->"+str(upper))
        elif lower == upper:
            res.append(str(upper))

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findMissingRanges([-1],-1,0))