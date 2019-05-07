//
// Created by 黄敏辉 on 2019-04-30.
//

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == nums[i-1])
                count ++;
            else
                nums[i - count] = nums[i];
        }
        return nums.size() - count;
    }
};