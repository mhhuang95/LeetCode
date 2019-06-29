//
// Created by 黄敏辉 on 2019-06-28.
//

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        helper(res, "", n, 0);
        return res;
    }

    void helper(vector<srting> &res, string s, l, r){
        if (l == 0 && r == 0){
            res.push_back(s);
            return;
        }
        if (l > 0)
            helper(res, s + "(", l - 1, r + 1);
        if (r > 0)
            helper(res, s + ")", l , r - 1);
    }
};