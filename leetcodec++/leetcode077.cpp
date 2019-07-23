//
// Created by 黄敏辉 on 2019-07-23.
//

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> comb;
        helper(res, comb, k, n, 1);
        return res;
    }

    void helper(vector<vector<int>>& res, vector<int>& comb, int k, int n, int begin){
        if (comb.size() == k) {
            res.push_back(comb);
            return;
        }

        for (int i = begin; i <= n; i++){
            comb.push_back(i);
            helper(res, comb, k, n, i+1);
            comb.pop_back();
        }
    }
};