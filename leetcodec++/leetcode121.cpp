//
// Created by 黄敏辉 on 2019-08-07.
//

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1)
            return 0;
        int res = 0, low = prices[0];
        for (int i = 1; i < prices.size(); i++){
            res = max(res, prices[i] - low);
            low = min(low, prices[i]);
        }
        return res;
    }
};