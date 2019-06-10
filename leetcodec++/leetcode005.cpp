//
// Created by 黄敏辉 on 2019-06-10.
//

class Solution {
public:
    string longestPalindrome(string s) {
        int len = 0, start = 0;
        for (int i = 0; i < s.size(); i++){
            int j = 0;
            while (i - j >= 0 && i + j < s.size() && s[i-j] == s[i+j]){
                if (2 * j + 1 > len){
                    len = 2*j+1;
                    start = i - j;
                }
                j++;
            }
            j = 0;
            while (i - j >= 0 && i + j + 1 < s.size() && s[i-j] == s[i+j+1]){
                if (2 * j + 2 > len){
                    len = 2*j+2;
                    start = i - j;
                }
                j++;
            }
        }
        return s.substr(start, len);
    }
};