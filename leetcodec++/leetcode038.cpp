//
// Created by 黄敏辉 on 2019-05-06.
//

class Solution {
public:
    string countAndSay(int n) {
        string s = "1";
        int i = 1;
        while (i < n){
            i++;
            string cur = "";
            for (int k = 0; k < s.size(); k++){
                int count = 1;
                while (k+1 < s.size() && s[k] == s[k+1]){
                    count ++;
                    k++;
                }
                cur += to_string(count) + s[k];
            }
            s = cur;
        }
        return s;
    }
};