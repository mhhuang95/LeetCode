class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        l1, l2 = len(board), len(board[0])

        starts = self.find_start(board,word[0])
        for start in starts:
            rec = [[0 for _ in range(l2)] for _ in range(l1)]
            i,j = start
            rec[i][j] = 1
            if self.find(board,i,j,word[1:],rec):
                return True
        return False


    def find_start(self,board,s):
        res = []
        l1, l2 = len(board), len(board[0])
        for i in range(l1):
            for j in range(l2):
                if board[i][j] == s:
                    res.append([i,j])
        return res

    def find(self, board,i,j, word,rec):
        l1, l2 = len(board), len(board[0])
        if len(word) == 0:
            return True
        if i+1 < l1 and rec[i+1][j]==0 and board[i+1][j] == word[0]:
            rec[i + 1][j] = 1
            if self.find(board,i+1,j,word[1:],rec):
                return True
            else:
                rec[i + 1][j] = 0
        if i-1 >= 0 and rec[i-1][j]==0 and board[i-1][j] == word[0]:
            rec[i - 1][j] = 1
            if self.find(board,i-1,j,word[1:],rec):
                return True
            else:
                rec[i - 1][j] = 0
        if j+1 < l2 and rec[i][j+1]==0 and board[i][j+1] == word[0]:
            rec[i][j + 1] = 1
            if self.find(board,i,j+1,word[1:],rec):
                return True
            else:
                rec[i][j + 1] = 0
        if j-1 >= 0 and rec[i][j-1]==0 and board[i][j-1] == word[0]:
            rec[i][j - 1] = 1
            if self.find(board,i,j-1,word[1:],rec):
                return True
            else:
                rec[i][j - 1] = 0
        return False


class Solution1(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        height = len(board)
        width = len(board[0])

        def go(i, j, depth):
            if depth >= len(word):
                return True

            if i < 0 or i >= height or j < 0 or j >= width:
                return False

            if board[i][j] == word[depth]:
                board[i][j] = '-'
                found = go(i - 1, j, depth + 1) or \
                        go(i + 1, j, depth + 1) or \
                        go(i, j - 1, depth + 1) or \
                        go(i, j + 1, depth + 1)
                board[i][j] = word[depth]
                if found:
                    return True

            if depth == 0:
                return go(i, j + 1, depth) if j + 1 < width else go(i + 1, 0, depth)

            return False

        return go(0, 0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))
