//
// Created by 黄敏辉 on 2019-06-13.
//

class Solution {
public:
    int myAtoi(string str) {
        long res = 0;

        if (str.empty())
            return res;

        int sign = 1;
        int ind = str.find_first_not_of(' ');

        if (ind == -1)
            return res;

        if (str[ind] == '+' || str[ind] == '-') sign = str[ind++] == '+' ? 1 : -1;

        while (ind < str.length() && isdigit(str[ind])) {
            res = res * 10 + (str[ind++] - '0');
            if (res * sign > INT_MAX) return INT_MAX;
            if (res * sign < INT_MIN) return INT_MIN;
        }

        return res * sign;

    }
};