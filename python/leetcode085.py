class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        l, h, r = [0]*col, [0]*col, [col]*col
        i = 0
        res = 0
        while i < row:
            curr_l = 0
            curr_r = col
            for j in range(col):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            for j in range(col):
                if matrix[i][j] == '1':
                    l[j] = max(l[j], curr_l)
                else:
                    l[j] = 0
                    curr_l = j + 1
            for j in range(col-1, -1, -1):
                if matrix[i][j] == '1':
                    r[j] = min(r[j], curr_r)
                else:
                    r[j] = col
                    curr_r = j

            for j in range(col):
                res = max(res, (r[j]-l[j])*h[j])
            i += 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))