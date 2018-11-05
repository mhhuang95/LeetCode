class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        x = []
        y = []
        l1,l2 = len(matrix), len(matrix[0])
        for i in range(l1):
            for j in range(l2):
                if matrix[i][j] == 0:
                    if i not in x:
                        x.append(i)
                    if j not in y:
                        y.append(j)
        for t in x:
            matrix[t][:] = [0 for _ in range(l2)]
        for t in y:
            for j in range(l1):
                matrix[j][t] = 0

