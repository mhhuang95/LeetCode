class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ls = len(nums)
        res = []
        for i in range(ls+1):
            res = res + self.combine(nums, i)
        return res

    def combine(self, nums, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.comb(res,[],nums,k,0)
        return res


    def comb(self,res, pre, nums,k,start):
        if k == 0:
            res.append(list(pre))
        elif start<len(nums):
            pre.append(nums[start])
            self.comb(res, pre, nums, k-1, start+1)
            pre.pop()
            self.comb(res, pre, nums, k, start+1)

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))