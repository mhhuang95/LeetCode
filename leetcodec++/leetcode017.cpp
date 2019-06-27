//
// Created by 黄敏辉 on 2019-06-27.
//

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.size() == 0)
            return res;
        static const vector<string> keyboard{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        res.push_back("");
        for (int i = 0; i < digits.size(); i++){
            const string& candidate = keyboard[digits[i] - '0'];
            if(candidate.empty())
                continue;
            vector<string> tmp;
            for (int j = 0; j < candidate.size(); j++)
                for (int k = 0; k < res.size(); k++)
                    tmp.push_back(res[k] + candidate[j]);
            res.swap(tmp);
        }
        return res;
    }
};