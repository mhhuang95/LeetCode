//
// Created by 黄敏辉 on 2019-09-05.
//

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {

        int n = matrix.size();
        if(n == 0)
            return 0;
        int m = matrix[0].size();
        int dp[n+1][m+1];
        memset(dp, 0, sizeof(dp));
        int s = 0;

        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++){
                if (matrix[i-1][j-1] == '0'){
                    dp[i][j] = 0;
                }
                else{
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]));
                    s = max(s, dp[i][j]);
                }
            }
        }
        return s*s;
    }

};