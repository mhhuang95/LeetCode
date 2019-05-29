//
// Created by 黄敏辉 on 2019-05-29.
//

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int i, j;
        int n = matrix.size();
        int tmp;
        for (i = 0; i < (n-1)/2 + 1; i++){
            for (j = 0; j < n / 2; j++){
                tmp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][i];
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
                matrix[j][n-1-i] = matrix[i][j];
            }
        }
    }
};