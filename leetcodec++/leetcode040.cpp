//
// Created by 黄敏辉 on 2019-07-12.
//

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> comb;
        helper(candidates, target, res, comb, 0);
        return res;
    }

    void helper(vector<int>& candidates, int target, vector<vector<int>>& res, vector<int>& comb, int begin){
        if (target == 0){
            res.push_back(comb);
            return;
        }

        for (int i = begin; i < candidates.size() && target >= candidates[i]; i++){
            if (i == begin || candidates[i] != candidates[i-1]) {
                comb.push_back(candidates[i]);
                helper(candidates, target - candidates[i], res, comb, i + 1);
                comb.pop_back();
            }
        }
    }
};
