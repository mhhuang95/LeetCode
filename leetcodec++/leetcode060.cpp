//
// Created by 黄敏辉 on 2019-07-17.
//

class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> v;
        int fact = 1;
        for(int i = 1; i <= n; i++){
            fact *= i;
            v.push_back(i);
        }
        k--;

        string res = "";
        for(int i = 0; i < n; i++){
            fact /= (n-i);
            ans.push_back(v[k/fact] + '0');
            v.erase(v.begin + k/fact);
            k %= fact;
        }
        return res;
    }
};