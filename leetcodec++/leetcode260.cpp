//
// Created by 黄敏辉 on 2019-09-17.
//

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int axorb = 0;

        for (auto& i:nums){
            axorb ^= i;
        }

        int lastbit = axorb & (~(axorb - 1));

        int x = 0;
        for (auto& i:nums){
            if(i & lastbit){
                x ^= i;
            }
        }

        int y = axorb ^ x;

        return vector<int> {x, y};
    }
};