class Solution():
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ls = len(nums)
        res = nums[0] + nums[1]+nums[2]
        for i in range(ls - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ls - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return temp
                elif temp > target:
                    k = k - 1

                else:
                    j = j + 1
                if abs(temp - target) < abs(res - target):
                    res = temp
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
