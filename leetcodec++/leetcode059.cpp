//
// Created by 黄敏辉 on 2019-07-17.
//

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res;
        if(n<=0) return res;
        res.resize(n, vector<int>(n,0));

        int lr = 0, lc = -1;
        int dir = 0;
        int val = 1;
        vector<vector<int>> dirs = {{0,1}, {1,0}, {0,-1}, {-1, 0}};

        vector<int> nSteps = {n, n - 1};

        while(nSteps[dir%2]){

            for(int i = 0; i < nSteps[dir%2]; i++){
                lr += dirs[dir][0];
                lc += dirs[dir][1];
                res[lr][lc] = val;
                val += 1;
            }

            nSteps[dir%2]--;
            dir = (dir + 1)%4;
        }
        return res;
    }
};