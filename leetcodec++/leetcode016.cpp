//
// Created by 黄敏辉 on 2019-06-27.
//

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int res = 100000000;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size()-2; i++){
            int l = i+1, r = nums.size() - 1;
            while(l < r){
                if (nums[i] + nums[l] + nums[r] == target){
                    res = target;
                    return res;
                } else if (nums[i] + nums[l] + nums[r] > target){
                    if (nums[i] + nums[l] + nums[r] - target < abs(res - target))
                        res = nums[i] + nums[l] + nums[r];
                    r--;
                } else{
                    if (target - (nums[i] + nums[l] + nums[r]) < abs(res - target))
                        res = nums[i] + nums[l] + nums[r];
                    l++;
                }
            }
        }
        return res;
    }
};