//
// Created by 黄敏辉 on 2019-07-10.
//

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        int mid;
        while(start <= end){
            mid = (start + end) / 2;
            if(nums[mid] == target){
                int l = mid, r = mid;
                while(nums[start] != target && start < l){
                    if (nums[(start + l) / 2] == target)
                        l = (start + l) / 2;
                    else
                        start = (start + l) / 2 + 1;
                }
                while(nums[end] != target && r < end){
                    if (nums[(r + end + 1) / 2] == target)
                        r = (r + end + 1) / 2;
                    else
                        end = (r + end + 1) / 2 - 1;
                }
                return vector<int> {start, end};
            }
            else if(nums[mid] < target){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
        }
        return vector<int> {-1, -1};
    }
};