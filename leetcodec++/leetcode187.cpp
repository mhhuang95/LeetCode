//
// Created by 黄敏辉 on 2019-08-26.
//

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        int l = s.size();
        unordered_map<string, int> m;
        for (int i = 0; i < l;i++){
            string sub = s.substr(i, 10);
            if(m[sub] == 1)
                res.push_back(sub);
            m[sub] ++;
        }

        return res;
    }
};