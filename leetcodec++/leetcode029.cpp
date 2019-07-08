//
// Created by 黄敏辉 on 2019-07-06.
//

class Solution {
public:
    int divide(int dividend, int divisor) {
        int res = 0;
        int sign = 1;

        if(dividend == INT_MIN  && divisor == -1){
            return INT_MAX;
        }

        if(dividend > 0){
            dividend = -dividend;
            sign = -sign;
        }

        if(divisor > 0){
            divisor = -divisor;
            sign = -sign;
        }

        while(true){
            int tmp = divisor;
            int q = 1;

            if (dividend > tmp){
                return -sign*res;
            }

            while (dividend < tmp){
                res += -q;
                dividend -= tmp;
                if (dividend  >= tmp)
                    break;

                tmp = -((-tmp) << 1);
                q <<= 1;
            }

            if (dividend == tmp){
                res += -q;
                return -sign*res;
            }
        }
    }
};