class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ls = len(digits)
        for i in range(ls-1, -1, -1):
            curr,d = divmod(digits[i]+1, 10)
            if curr == 0:
                break
        if curr == 1:
            digits.insert(0,1)
        return digits