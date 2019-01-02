class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m,n = len(matrix), len(matrix[0])
        for i in range(1,m):
            matrix[i][0] += matrix[i-1][0]
        for j in range(1,n):
            matrix[0][j] += matrix[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] += matrix[i-1][j]+matrix[i][j-1] - matrix[i-1][j-1]
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        mat = self.matrix
        if row1 == 0 and col1 == 0:
            return mat[row2][col2]
        elif row1 == 0:
            return mat[row2][col2] - mat[row2][col1-1]
        elif col1 == 0:
            return mat[row2][col2] - mat[row1-1][col2]
        return mat[row2][col2]- mat[row1-1][col2] - mat[row2][col1-1] + mat[row1-1][col1-1]




        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
if __name__ == "__main__":
    s = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(s.sumRegion(2,1,4,3))