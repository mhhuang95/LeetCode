//
// Created by 黄敏辉 on 2019-05-12.
//

class Solution {
public:
    bool isPowerOfFour(int num) {
        return num > 0 && (num & (num-1)) == 0 && (num-1)%3 == 0;
    }
};