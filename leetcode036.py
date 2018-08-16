class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for x in board:
            if self.judge(x) == False:
                return False
        for i in range(9):
            x = []
            for j in range(9):
                x.append(board[j][i])
            if self.judge(x) == False:
                return False
        for i in range(3):
            for j in range(3):
                x = []
                for m in range(3):
                    for n in range(3):
                        x.append(board[3*i+m][3*j+n])
                if self.judge(x) == False:
                    return False
        return True

    def judge(self, nums):
        l = []
        for x in nums:
            if ord(x)>=ord('0') and ord(x) <= ord('9'):
                l.append(x)
        s = set(l)
        if len(l) == len(s):
            return True
        else:
            return False
