//
// Created by 黄敏辉 on 2019-06-08.
//

class Solution {
public:
    string multiply(string num1, string num2) {
        int n1, n2, p;

        int l1 = num1.size(), l2 = num2.size();

        vector<int> v(l1+l2, 0);

        if (l1 == 0 || l2 == 0)
            return "0";

        for (int i = 0; i < l1; i++){
            int carry = 0;
            n1 = (int)(num1[l1 - i - 1] - '0');
            for(int j = 0; j < l2; j++){
                n2 = (int)(num2[l2 - j - 1] - '0');
                p = n1 * n2 + v[i+j] + carry;

                carry = p / 10;
                v[i+j] = p % 10;
            }
            if (carry > 0){
                v[i + l2] = carry;
            }

        }

        int start = l1 + l2 - 1;
        while (start >= 0 && v[start] == 0){
            start--;
        }
        if (start == -1){
            return "0";
        }

        string res = "";
        while(start >= 0){
            res += (char)(v[start] + '0');
            start--;
        }
        return res;
    }
};
