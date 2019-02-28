class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])

        def sink(i, j, s1, s2):
            if 0 <= i < m and 0 <= j < n and board[i][j] == s1:
                board[i][j] = s2
                sink(i, j + 1,s1,s2)
                sink(i, j - 1,s1,s2)
                sink(i + 1, j,s1,s2)
                sink(i - 1, j,s1,s2)

        for i in range(m):
            sink(i, 0, 'O', '1')
            sink(i, n - 1, 'O', '1')
        for i in range(n):
            sink(0, i, 'O', '1')
            sink(m - 1, i, 'O', '1')
        board[:] = [['XO'[c == '1'] for c in row] for row in board]



if __name__ == "__main__":
    s = Solution()
    s.solve()