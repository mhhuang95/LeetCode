//
// Created by 黄敏辉 on 2019-09-18.
//

class Solution {
public:
    int hIndex(vector<int>& citations) {
        if (citations.size() == 0)
            return 0;
        sort(citations.begin(), citations.end(), greater<int>());
        int i = 0;
        while(i < citations.size() && citations[i] > i)
            i++;
        return i;
    }
};