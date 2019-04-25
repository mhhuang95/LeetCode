//
// Created by 黄敏辉 on 2019-04-25.
//

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;


class leetcode001 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            if (hash.find(target - nums[i]) != hash.end()){
                res.push_back(hash[target - nums[i]]);
                res.push_back(i);
                break;
            }
            hash[nums[i]] = i;
        }
        return res;
    }
};
