//
// Created by 黄敏辉 on 2019-08-27.
//

class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int mask = 0xFFFFFFFF;
        for(; (n&mask) != (m&mask); mask <<=1);
        return m&mask;
    }
};