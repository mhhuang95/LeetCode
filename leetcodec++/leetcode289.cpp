//
// Created by 黄敏辉 on 2019-09-19.
//

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        for(int i = 0; i < m;i++ ){
            for (int j = 0; j < n; j++){
                int numNei = countNeighbors(board, i, j);
                if (board[i][j] == 1 && (numNei < 2 || numNei > 3))
                    board[i][j] = 3;
                else if (board[i][j] == 0 && numNei == 3)
                    board[i][j] = 4;
            }
        }
        for(int i = 0; i < m;i++ ) {
            for (int j = 0; j < n; j++) {
                if(board[i][j] == 3)
                    board[i][j] = 0;
                if(board[i][j] == 4)
                    board[i][j] = 1;
            }
        }
    }

    int countNeighbors(vector<vector<int>>& board, int i, int j){
        int count = 0;
        int m = board.size();
        int n = board[0].size();
        int d[][2] = {{1,-1},{1,0},{1,1},{0,-1},{0,1},{-1,-1},{-1,0},{-1,1}};

        for(int k = 0; k < 8; k++){
            int x = d[k][0] + i;
            int y = d[k][1] + j;
            if(x < 0 || x >= m || y < 0 || y >= n) {
                continue;
            }
            if(board[x][y] & 1) {
                count++;
            }
        }
        return count;
    }
};