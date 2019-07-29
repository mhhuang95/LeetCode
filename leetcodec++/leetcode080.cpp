//
// Created by 黄敏辉 on 2019-07-29.
//

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 1;
        for (int i = 1;i < nums.size(); ){
            if (nums[i] != nums[i-1]) {
                count = 1;
                i++;
            }
            else if (nums[i] == nums[i-1] && count == 1) {
                count += 1;
                i++;
            }
            else if (nums[i] == nums[i-1] && count == 2)
                nums.erase(nums.begin() + i);
        }
        return nums.size();
    }
};

