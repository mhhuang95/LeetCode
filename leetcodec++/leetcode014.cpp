//
// Created by 黄敏辉 on 2019-04-26.
//

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";
        string s = strs[0];
        for (int i = 0; i < strs.size(); i++){
            while (strs[i].find(s) != 0){
                s = s.substr(0, s.length()-1);
                if (s.length() == 0) return "";
            }
        }
        return s;
    }
};