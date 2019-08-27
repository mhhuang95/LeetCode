//
// Created by 黄敏辉 on 2019-08-27.
//

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(),n;
        if (m == 0)
            return 0;
        n = grid[0].size();
        int res = 0;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (grid[i][j] == '1') {
                    eraseIsland(grid, i,j);
                    res++;
                }
            }
        }
        return res;
    }

    void eraseIsland(vector<vector<char>>& grid, int i, int j){
        int m = grid.size(), n = grid[0].size();
        if (i < 0 || i == m || j < 0 || j == n || grid[i][j] == '0')
            return;
        grid[i][j] = '0';
        eraseIsland(grid, i-1, j);
        eraseIsland(grid, i+1, j);
        eraseIsland(grid, i, j-1);
        eraseIsland(grid, i, j+1);
    }
};