//
// Created by 黄敏辉 on 2019-07-30.
//

class Solution {
public:
    int numDecodings(string s) {
        int l = s.length(), last, next_last, res;
        if(s[0] == '0') return 0;
        if(s.size() == 1) return 1;
        last = next_last = 1;
        for (int i = 1;i < l;i++){
            if(s[i] == '0') {
                if(s[i-1] >= '3' || s[i-1] == '0') return 0;
                else res = next_last;
            }
            else if (s[i-1] == '1' || s[i-1] == '2' && s[i] <= '6')
                res = last + next_last;
            else
                res = last;
            next_last = last;
            last = res;
        }
        return res;
    }
};