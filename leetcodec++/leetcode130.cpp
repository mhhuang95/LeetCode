//
// Created by 黄敏辉 on 2019-08-07.
//

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int l1 = board.size();
        int l2 = board.front().size();
        for (int i = 0; i < l1; i++)
            sink(board, i, 0);
        for (int i = 0; i < l1; i++)
            sink(board, i, l2-1);
        for (int i = 0; i < l2; i++)
            sink(board, 0, i);
        for (int i = 0; i < l2; i++)
            sink(board, l1-1, i);

        for (int i = 1; i < l1-1; i++){
            for (int j = 1; j < l2 - 1; j++){
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
            }
        }

        for (int i = 0; i < l1; i++){
            for (int j = 0; j < l2 ; j++){
                if (board[i][j] == 'S')
                    board[i][j] = 'O';
            }
        }
    }

    void sink(vector<vector<int>>& board, int i, int j){
        if (board[i][j] == 'O'){
            board[i][j] = 'S';
            if (i >= 1)
                sink(board, i-1, j, c1, c2);
            if (i < board.size()-1)
                sink(board, i+1, j, c1, c2);
            if (j >= 1)
                sink(board, i, j-1, c1, c2);
            if (j < board.front().size()-1)
                sink(board, i, j+1, c1, c2);
        }
    }
};