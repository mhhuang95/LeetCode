//
// Created by 黄敏辉 on 2019-07-19.
//

class Solution {
public:
    const int LetMeBe = -65435643;
    void setZeroes(vector<vector<int>>& matrix) {
        for (int i(0); i < matrix.size(); i ++){
            for(int j(0); j < matrix[0].size(); j++){
                if (matrix[i][j] == 0)
                    matrix[i][j] = LetMeBe;
            }
        }
        for (int i(0); i < matrix.size(); i ++){
            for(int j(0); j < matrix[0].size(); j++){
                if (matrix[i][j] == LetMeBe) {
                    helper(matrix, i, j);
                    matrix[i][j] = 0;
                }
            }
        }
    }

    void helper(vector<vector<int>>& matrix, int i, int j){
        for (int k(0);  k < matrix[0].size(); k++){
            if (matrix[i][k] != LetMeBe)
                matrix[i][k] = 0;
        }
        for (int k(0); k < matrix.size(); k ++){
            if(matrix[k][j] != LetMeBe)
                matrix[k][j] = 0;
        }

    }
};
