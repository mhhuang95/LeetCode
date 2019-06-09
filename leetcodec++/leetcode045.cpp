//
// Created by 黄敏辉 on 2019-06-08.
//

class Solution {
public:
    int jump(vector<int>& nums) {
        int ls = nums.size();
        int start, end, maxdis, step;

        if (ls <= 1){
            return 0;
        }

        start = 0;
        end = nums[0];
        maxdis = nums[0];
        step = 1;

        while (end < ls - 1){
            for (int i = start + 1; i < end + 1; i++){
                if (maxdis <  i + nums[i])
                    maxdis = i + nums[i];
            }
            start = end;
            end = maxdis;
            step++;
        }
        return step;
    }
};