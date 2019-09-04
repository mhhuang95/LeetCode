//
// Created by 黄敏辉 on 2019-09-03.
//

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> idx;
        for (int i = 0; i < nums.size(); i++){
            if (idx.count(nums[i]) == 0)
                idx[nums[i]] = i;
            else if ( i - idx[nums[i]] <= k)
                return true;
            else
                idx[nums[i]] = i;
        }
        return false;
    }
};