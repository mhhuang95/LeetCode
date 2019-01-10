class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n,l = len(A), len(A[0]), len(B[0])
        res = [[0]*l for i in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(l):
                        if B[j][l] != 0:
                            res[i][l] += A[i][j]*B[j][l]
        return res