//
// Created by 黄敏辉 on 2019-05-06.
//

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        while (i < nums.size()){
            if (nums[i] == val){
                nums.erase(nums.begin() + i);
            }else
                i++;
        }
        return nums.size();
    }
};