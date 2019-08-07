//
// Created by 黄敏辉 on 2019-08-06.
//

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>> dp;
        vector<int> row;
        for (int i = 0; i < triangle.size(); i++){
            row = triangle[i];
            if (i >= 1){
                row[0] += dp[dp.size()-1][0];
                row[row.size()-1] +=  dp[dp.size()-1][dp[dp.size()-1].size()-1];
                for (int j = 1; j < row.size()-1;j++)
                    row[j] += min(dp[dp.size()-1][j-1] ,  dp[dp.size()-1][j]);
            }
            dp.push_back(row);
        }
        row = dp[dp.size() - 1];
        return *min_element(row.begin(), row.end());
    }
};