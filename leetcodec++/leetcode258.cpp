//
// Created by 黄敏辉 on 2019-09-17.
//

class Solution {
public:
    int addDigits(int num) {
        while(num / 10 > 0){
            int tmp = 0;
            while (num > 0){
                tmp += num % 10;
                num /= 10;
            }
            num = tmp;
        }
        return num;
    }
};