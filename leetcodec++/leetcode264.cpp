//
// Created by 黄敏辉 on 2019-09-18.
//

class Solution {
public:
    int nthUglyNumber(int n) {
        if (n <= 0)
            return false;
        if (n == 1)
            return true;
        int e2 = 0, e3 = 0, e5 = 0;
        vector<int>k(n);
        k[0] = 1;
        for(int i = 1; i < n; i++){
            k[i] = min(k[e2] * 2, min(k[e3] * 3, k[e5] * 5));
            if(k[i] == k[e2] * 2) e2++;
            if(k[i] == k[e3] * 3) e3++;
            if(k[i] == k[e5] * 5) e5++;
        }
        return k[n-1];
    }
};