class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ls = len(triangle)
        total = triangle[0]
        for i in range(ls-1):
            temp = triangle[i+1]
            for j in range(len(temp)):
                if j == 0:
                    temp[j] += total[j]
                elif j == len(temp)-1:
                    temp[j] += total[j-1]
                else:
                    temp[j] = min(temp[j]+total[j], temp[j]+total[j-1])
            total = temp
        return min(total)
