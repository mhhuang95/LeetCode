//
// Created by 黄敏辉 on 2019-09-02.
//

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int res = 0;
        int start = 0, end = 0;
        int sum = 0;
        while (end < nums.size()){
            sum += nums[end];
            end++;
            if (sum >= s){
                if (res == 0)
                    res = end - start;
                else
                    res = min(res, end - start);
            }
            while (sum - nums[start] >= s){
                sum -= nums[start];
                start++;
                res = min(res, end - start);
            }
        }
        return res;
    }
};