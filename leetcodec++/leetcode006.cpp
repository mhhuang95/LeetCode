//
// Created by 黄敏辉 on 2019-06-10.
//

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1)
            return s;

        int ls = s.length();
        string *str = new string[numRows];

        int step = 1, row = 0;
        for (int i = 0; i < ls; i++){
            str[row] += s[i];

            if (row == 0)
                step = 1;
            if (row == numRows - 1)
                step = -1;

            row += step;
        }
        s.clear();
        for (int j = 0; j < numRows; j++){
            s += str[j];
        }
        return s;
    }
};