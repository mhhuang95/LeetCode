//
// Created by 黄敏辉 on 2019-07-08.
//


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int l = nums.size();
        int i = l - 1, j = i;
        while (i > 0 && nums[i] <= nums[i-1]){
            i--;
        }
        if (i == 0) {
            sort(nums.begin(), nums.end());
            return;
        }
        while (nums[j] <= nums[i-1]){
            j --;
        }
        swap(nums[i-1], nums[j]);
        sort(nums.end() - (l-i), nums.end());
        return;
    }
};