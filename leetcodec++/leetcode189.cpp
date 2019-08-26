//
// Created by 黄敏辉 on 2019-08-26.
//

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        for (int i = 0; i < k; i++){
            int t = nums.back();
            nums.pop_back();
            nums.insert(nums.begin(), t);
        }
    }
};