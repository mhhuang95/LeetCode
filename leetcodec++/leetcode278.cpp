//
// Created by 黄敏辉 on 2019-05-09.
//

// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int lower = 1, upper = n, mid;
        while (lower < upper){
            mid = lower + (upper - lower) / 2;
            if (!isBadVersion(mid))
                lower = mid +1;
            else
                upper = mid;
        }
        return lower;
    }
};