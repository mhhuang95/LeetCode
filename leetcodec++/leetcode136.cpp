//
// Created by 黄敏辉 on 2019-08-12.
//

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < nums.size(); i++)
            res ^= nums[i];
        return res;
    }
};