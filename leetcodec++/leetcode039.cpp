//
// Created by 黄敏辉 on 2019-07-11.
//

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        sort(candidates.begin(), candidates.end());
        vector<int> comb;
        helper(candidates, target, res, comb, 0);
        return res;
    }

    void helper(vector<int>& candidates, int target, vector<vector<int>>& res, vector<int> comb, int begin){
        if (target == 0){
            res.push_back(comb);
            return;
        }

        for(int i = begin; i != candidates.size() && candidates[i] <= target; i++){
            comb.push_back(candidates[i]);
            helper(candidates, target - candidates[i], res, comb, i);
            comb.pop_back();
        }
    }
};