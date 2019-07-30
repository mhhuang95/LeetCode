//
// Created by 黄敏辉 on 2019-07-30.
//

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res{0};
        for (int i = 0; i < n; i++){
            int ls = res.size();
            for (int k = ls-1; k >= 0; k--){
                res.push_back(res[k] + pow(2,i));
            }
        }
        return res;
    }
};