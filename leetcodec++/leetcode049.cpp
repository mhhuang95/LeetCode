//
// Created by 黄敏辉 on 2019-05-29.
//


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ret;

        if (strs.empty())
            return ret;

        unordered_map<string,vector<string>> mp;

        for (string s:strs)
        {
            int count[26] = {0};
            for (char c:s)
            {
                count[c - 'a']++;
            }
            string key;
            for (int k:count)
                key += ('#' + k);

            mp[key].push_back(s);
        }

        for (auto p:mp)
            ret.push_back(p.second);

        return ret;
    }
};