//
// Created by 黄敏辉 on 2019-08-08.
//

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int carry = 0;
        pair<size_t, int> city_carry(0, 0);
        for (size_t i = 1; i < gas.size(); ++i) {
            carry += gas[i - 1] - cost[i - 1];
            if (carry < city_carry.second) {
                city_carry = {i, carry};
            }
        }
        carry += gas[gas.size()-1] - cost[gas.size()-1];
        return carry >= 0 ? city_carry.first : -1;
    }
};