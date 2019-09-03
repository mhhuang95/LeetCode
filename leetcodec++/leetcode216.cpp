//
// Created by 黄敏辉 on 2019-09-02.
//

class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> comb;
        find_comb(res,comb, k, n);
        return res;
    }

    void find_comb(vector<vector<int>>& res, vector<int>& comb, int k ,int n){
        if(comb.size() == k && n == 0){
            res.push_back(comb);
            return;
        }
        if(comb.size() < k){
            for (int i = comb.empty()? 1:comb.back()+1; i <= 9;i++){
                if (n - i < 0)
                    break;
                comb.push_back(i);
                find_comb(res, comb, k, n-i);
                comb.pop_back();
            }
        }
    }
};