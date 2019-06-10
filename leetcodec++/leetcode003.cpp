//
// Created by 黄敏辉 on 2019-06-09.
//

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int res = 0, start = -1;
        for (int i = 0; i < s.size(); i++){
            if (dict[s[i]] > start)
                start = dict[s[i]];
            res = max(res, i - start);
            dict[s[i]] = i;
        }
        return res;

    }
};