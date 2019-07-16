//
// Created by 黄敏辉 on 2019-07-16.
//

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len = nums.size();
        if (len == 1)
            return true;
        int pos = 0;
        int max_dis = nums[0];

        while (max_dis < len-1){
            int flag = 0;
            for (int i = pos; i <= pos + nums[pos]; i++){
                if (i + nums[i] > max_dis){
                    pos = i;
                    max_dis = i + nums[i];
                    flag = 1;
                    break;
                }
            }
            if (!flag)
                return false;
        }
        return true;
    }
};