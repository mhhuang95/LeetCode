class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        neigh = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        def count_live(i,j):
            count = 0
            for a,b in neigh:
                if 0 <= i+a < m and 0 <= j+b < n and board[i+a][j+b] % 2 == 1:
                    count += 1
            return count

        for i in range(m):
            for j in range(n):
                lives = count_live(i, j)
                if board[i][j] == 1:
                    if lives < 2 or lives > 3:
                        board[i][j] = 3
                else:
                    if lives == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

