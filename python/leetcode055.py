class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        ls = len(nums)
        if nums[0] >= ls-1:
            return True
        if nums[0]==0:
            return False
        for i in range(1,nums[0]+1):
            if self.canJump(nums[i:]):
                return True
        return False
        '''
        length = len(nums)
        begin = length-1
        for i in reversed(range(length-1)):
            if i + nums[i] >= begin:
                begin = i
        return not begin

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([1,2,3]))