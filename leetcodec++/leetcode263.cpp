//
// Created by 黄敏辉 on 2019-09-18.
//

class Solution {
public:
    bool isUgly(int num) {
        if (num == 0)
            return false;
        while (num % 2 == 0)
            num /= 2;
        while (num % 3 == 0)
            num /= 3;
        while (num % 5 == 0)
            num /= 5;
        return num==1;
    }
};