//
// Created by 黄敏辉 on 2019-07-29.
//

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = nums.size();
        int s = 0, e = l-1;
        int mid;
        while(s <= e){
            while (s < e && nums[s] == nums[s + 1]) {
                s++;
            }
            while (s < e && nums[e] == nums[e - 1]) {
                e--;
            }
            mid = (s+e) / 2;
            if(nums[mid] == target)
                return true;
            else if (nums[mid] < target){
                if (nums[e] >= target || nums[e] < nums[mid])
                    s = mid + 1;
                else
                    e = mid - 1;
            }else if (nums[mid] > target){
                if (nums[s] <= target || nums[s] > nums[mid])
                    e = mid - 1;
                else
                    s = mid + 1;
            }
        }
        return false;
    }
};