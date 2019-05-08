//
// Created by 黄敏辉 on 2019-05-08.
//

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while(n){
            n = n&(n-1);
            count ++;
        }
        return count;
    }
};