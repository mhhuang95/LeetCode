//
// Created by 黄敏辉 on 2019-09-18.
//

class Solution {
public:
    int hIndex(vector<int>& citations) {
        if (citations.empty())
            return 0;
        int start = 0, len = citations.size(), end = len - 1;
        while (start <= end){
            int mid = (start + end) / 2;
            if (citations[mid] < len - mid)
                start = mid + 1;
            else if (citations[mid] > len - mid)
                end = mid - 1;
            else
                return len - mid;
        }
        return len - start;
    }
};