class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls = len(numbers)
        i = 0
        j = ls-1
        while i < j:
            if numbers[i]+numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j] < target:
                i += 1
            else:
                j -= 1

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15],9))