class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        blank = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blank.append([i,j])
        self.fillin(board, blank)

    def fillin(self,board, blank):
        ls = len(blank)
        if ls == 0:
            return True
        [row, col] = blank[-1]
        for k in range(1,10):
            if self.isValid(board, row, col, str(k)):
                board[row][col] = str(k)
                blank.pop()
                if self.fillin(board, blank):
                    return True
                board[row][col] = '.'
                blank.append([row, col])
        return False


    def isValid(self, board, row, col, ch):
        for j in range(9):
            if board[j][col] == ch:
                return False
            if board[row][j] == ch:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == ch:
                    return False
        return True
