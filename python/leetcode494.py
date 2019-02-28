class Solution(object):
    def findTargetSumWays1(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nums.sort()
        cache = {}
        return self.helper(nums, S,cache)

    def helper(self, nums, target,cache):
        if len(nums) == 1:
            if nums[0] == target or nums[0] == (-target):
                return 1
            else:
                return 0
        key = self.gen_key(nums,target)
        if key in cache:
            return cache[key]
        else:
            cache[key] = 0

        for i in range(0, len(nums)):
            if i >= 1 and nums[i]==nums[i-1]:
                continue
            l = nums[:i]+nums[i+1:]
            key1 = self.gen_key(l,target+nums[i])
            if key1 in cache:
                res1 = cache[key1]
            else:
                res1 = self.helper(l,target+nums[i],cache)
            key2 = self.gen_key(l,target-nums[i])
            if key2 in cache:
                res2 = cache[key2]
            else:
                res2 = self.helper(l, target - nums[i], cache)
            cache[key] += res1+res2
        return cache[key]

    def gen_key(self,nums, target):
        tmp = [str(x) for x in nums]
        tmp.append(str(target))
        return ' '.join(tmp)

    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]:1, -nums[0]:1} if nums[0]!= 0 else {0:2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d+nums[i]] = tdic.get(d+nums[i],0) + dic.get(d,0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S,0)



if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays([1,0],1))