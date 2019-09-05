//
// Created by 黄敏辉 on 2019-09-05.
//

class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        long total = (C-A)*(D-B) + (G-E)*(H-F);
        long x1 = max(E,A), y1 = max(F,B), x2 = min(G,C), y2 = min(H,D);
        if(x2-x1<=0 || y2-y1<=0) return total;
        long sub = (long)(x2-x1)*(y2-y1);
        return total - sub;
    }
};