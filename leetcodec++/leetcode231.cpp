//
// Created by 黄敏辉 on 2019-09-15.
//

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0) return false;
        return !(n&(n-1));
    }
};