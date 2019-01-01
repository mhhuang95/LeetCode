class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        one = float("-inf")
        two = float("-inf")
        three = float("-inf")

        for x in nums:
            if x > one:
                three = two
                two = one
                one = x
            elif x > two:
                three = two
                two = x
            elif x > three:
                three = x

        if three == float("-inf"):
            return one
        else:
            return three