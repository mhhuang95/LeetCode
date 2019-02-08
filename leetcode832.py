class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        m,n = len(A), len(A[0])
        def flip(l):
            for k in range(n//2):
                l[k], l[n-1-k] =  l[n-1-k], l[k]
        for i in range(m):
            flip(A[i])
        for i in range(m):
            for j in range(n):
                A[i][j] = (0,1)[A[i][j]==0]

        return A