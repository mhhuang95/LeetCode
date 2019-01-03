class Solution:
    def canPartition(self, nums):

        
        if sum(nums) % 2 == 1:
            return False
        half_sum = sum(nums) / 2
        nums_length = len(nums)

        visited = {}

        def recurse(n, s):
            key = str((n , s))
            if n >= nums_length or s > half_sum:
                return False
            if s == half_sum:
                return True
            if key in visited:
                return visited[key]
            visited[key] = recurse(n + 1, s + nums[n]) or recurse(n + 1, s)
            if (visited[key]):
                return  True
            return False

        return recurse(0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1,2,3,4,5,6,7]))