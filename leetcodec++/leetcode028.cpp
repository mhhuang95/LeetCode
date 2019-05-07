//
// Created by 黄敏辉 on 2019-05-06.
//

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.size() == 0)
            return 0;
        int res = haystack.find(needle);
        if (res < haystack.size())
            return res;
        else
            return -1;
    }
};