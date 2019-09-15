//
// Created by 黄敏辉 on 2019-09-15.
//

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        int p = 1;
        for (int i = 0; i < nums.size(); i++){
            res.push_back(p);
            p *= nums[i];
        }
        p = 1;
        for (int i = nums.size() - 1; i >= 0; i--){
            res[i]  *= p;
            p *= nums[i];
        }
        return res;
    }
};