//
// Created by 黄敏辉 on 2019-07-09.
//

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        int l = 0, r = len-1;
        int mid;
        while (l <= r){
            mid = (r + l) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] >= nums[0]){
                if (target >= nums[0] && target < nums[mid])
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            else{
                if (target > nums[mid] && target <= nums[r])
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return -1;
    }
};