//
// Created by 黄敏辉 on 2019-08-12.
//

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int> t(32);
        int i,j,n;
        for (i = 0; i < nums.size(); i++){
            n = nums[i];
            for (j = 31; j >= 0 ;j--){
                t[j] += n & 1;
                n >>= 1;
                if (!n)
                    break;
            }
        }
        int res = 0;
        for (j = 31; j >= 0; j--){
            n = t[j] % 3;
            if (n)
                res += 1 << (31 - j);
        }
        return res;
    }
};