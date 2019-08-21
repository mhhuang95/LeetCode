//
// Created by 黄敏辉 on 2019-08-21.
//

class Solution {
public:
    int findMin(vector<int>& nums) {
        int i = 0, j = nums.size()-1;
        int mid;
        while (i < j){
            if (nums[i] < nums[j])
                return nums[i];

            mid = (i + j) / 2;

            if (nums[mid] >= nums[i])
                i = mid + 1;
            else
                j = mid;
        }
        return nums[i];
    }
};