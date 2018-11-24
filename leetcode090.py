class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        begin = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                begin = 0
            size = len(res)
            for j in range(begin,size):
                curr = list(res[j])
                curr.append(nums[i])
                res.append(curr)
            begin = size

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))