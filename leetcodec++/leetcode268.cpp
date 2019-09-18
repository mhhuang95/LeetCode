//
// Created by 黄敏辉 on 2019-09-18.
//

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = nums.size();
        int i = 0;
        for (int n:nums){
            res ^= n;
            res ^= i;
            i++;
        }
        return res;
    }
};