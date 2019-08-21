//
// Created by 黄敏辉 on 2019-08-21.
//

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int front = 1;
        int back = 1;
        int res = INT_MIN;
        int l = nums.size();
        for (int i = 0; i < l; i++){
            front *= nums[i];
            back *= nums[l - 1 - i];
            res = max(res, max(front, back));
            front = front == 0 ? 1 : front;
            back = back == 0 ? 1 : back;
        }
        return res;
    }
};