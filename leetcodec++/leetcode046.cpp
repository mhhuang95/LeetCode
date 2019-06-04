//
// Created by 黄敏辉 on 2019-05-29.
//

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        helper(res, nums, 0);
        return res;
    }

    void helper(vector<vector<int>>& res, vector<int>& nums, int index){

        if (index >= nums.size()){
            res.push_back(nums);
            return;
        }

        for (int i = index; i < nums.size(); i++){
            swap(nums[i], nums[index]);
            helper(res, nums, index + 1);
            swap(nums[i], nums[index]);
        }
    }
};