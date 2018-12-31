class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ls = len(nums)
        res = ls+1
        start = 0
        end = 0
        val = 0
        while end < ls:
            while val < s:
                val += nums[end]
                end += 1

            while val >= s:

                res = min(res, end - start)
                val -= nums[start]
                start += 1

        return 0 if res == ls+1 else res

if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
