class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        prev = self.generate(numRows-1)
        temp = [1]*(len(prev[-1])+1)
        for i in range(len(prev[-1])-1):
            temp[i+1] = prev[-1][i] + prev[-1][i+1]
        prev.append(temp)
        return prev

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))