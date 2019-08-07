//
// Created by 黄敏辉 on 2019-08-07.
//

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1)
            return 0;
        int res = 0, low = prices[0], i = 1;
        while(i < prices.size()){
            while(i < prices.size() && prices[i] >= prices[i-1]){
                i++;
            }
            res += prices[i-1] - low;
            if (i < prices.size())
                low = prices[i];
            i++;
        }
        return res;
    }
};