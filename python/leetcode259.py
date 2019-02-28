class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ls=len(nums)
        res = 0
        for k in range(1, ls-1):
            i,j = 0,ls-1
            while i < k and j > k:
                if nums[i]+nums[k]+nums[j] < target:
                    res += j-k
                    i +=1
                else:
                    j -=1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumSmaller([0,-4,-1,1,-1,2],-5))