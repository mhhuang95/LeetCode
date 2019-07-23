//
// Created by 黄敏辉 on 2019-07-23.
//

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> comb;
        helper(res, comb, nums, 0);
        return res;
    }

    void helper(vector<vector<int>>& res, vector<int>& comb, vector<int> nums, int begin){
        res.push_back(comb);

        for (int i = begin; i < nums.size(); i++){
            comb.push_back(nums[i]);
            helper(res, comb, nums, i+1);
            comb.pop_back();
        }
    }
};