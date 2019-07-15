//
// Created by 黄敏辉 on 2019-07-15.
//

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<vector<int>> dirs{{0,1}, {1,0}, {0, -1}, {-1, 0}};
        vector<int> res;
        int l1 = matrix.size();
        if (l1 == 0){
            return res;
        }
        int l2 = matrix[0].size();
        if (l2 == 0){
            return res;
        }

        vector<int> Nsteps{l2, l1-1};

        int idir = 0;
        int ir = 0, ic = -1;
        while (Nsteps[idir % 2]){
            for (int i = 0; i < Nsteps[idir % 2]; i++){
                ir += dirs[idir][0];
                ic += dirs[idir][1];
                res.push_back(matrix[ir][ic]);
            }
            Nsteps[idir%2]--;
            idir = (idir + 1) % 4;

        }
        return res;
    }
};