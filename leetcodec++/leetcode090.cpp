//
// Created by 黄敏辉 on 2019-07-30.
//

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> comb;
        helper(res, nums, comb, 0);
        return res;
    }

    void helper(vector<vector<int>>& res, vector<int>& nums, vector<int>& comb, int begin){
        res.push_back(comb);
        for (int i = begin; i<nums.size();i++){
            if (i ==begin || nums[i] != nums[i-1]){
                comb.push_back(nums[i]);
                helper(res, nums, comb, i+1);
                comb.pop_back();
            }
        }
    }
};