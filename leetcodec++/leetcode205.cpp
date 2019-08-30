//
// Created by 黄敏辉 on 2019-08-30.
//

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> s_t;
        unordered_map<char, char> t_s;

        int l1 = s.size();
        int l2 = t.size();

        if (l1 != l2)
            return false;

        for(int i = 0; i < l1; i++){
            if (s_t.find(s[i]) == s_t.end() && t_s.find(t[i]) == t_s.end()){
                s_t[s[i]] = t[i];
                t_s[t[i]] = s[i];
            } else if ( (s_t.find(s[i]) == s_t.end() && t_s.find(t[i]) != t_s.end()) || (s_t.find(s[i]) != s_t.end() && t_s.find(t[i]) == t_s.end()))
                return false;
            else if (s_t[s[i]] != t[i] || t_s[t[i]] != s[i])
                return false;
        }
        return true;
    }
};