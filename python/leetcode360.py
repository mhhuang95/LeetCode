class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x):
            return a * x ** 2 + b * x + c

        res = []
        p1, p2 = 0, len(nums)-1
        nums = list(map(f, nums))
        if a < 0:
            while p2>=p1:
                if nums[p1] < nums[p2]:
                    res.append(nums[p1])
                    p1+=1
                else:
                    res.append(nums[p2])
                    p2-=1
        else:
            while p2>=p1:
                if nums[p1] < nums[p2]:
                    res.insert(0, nums[p2])
                    p2-=1
                else:
                    res.insert(0, nums[p1])
                    p1+=1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.sortTransformedArray([-4,-2,2,4],-1,3,5))