//
// Created by 黄敏辉 on 2019-09-18.
//

class Solution {
public:
    int numSquares(int n) {
        vector<int> dp{0};
        while (dp.size() <= n){
            int m = dp.size(), s = INT_MAX;
            for (int i = 1; i*i <= m; i++)
                s = min(s, dp[m - i*i] + 1);
            dp.push_back(s);
        }
        return dp[n];
    }
};