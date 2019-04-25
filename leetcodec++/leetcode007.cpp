//
// Created by 黄敏辉 on 2019-04-25.
//
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;


class Solution {
public:
    int reverse(int x) {
        long int res = 0;

        while (x != 0){
            res = res * 10 + x%10;
            x = x / 10;
            if(res > INT_MAX)
                return 0;
            if(res <INT_MIN)
                return 0;
        }
        return res;
    }
};