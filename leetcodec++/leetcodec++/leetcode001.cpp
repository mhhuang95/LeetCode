//
//  leetcode001.cpp
//  leetcodec++
//
//  Created by 黄敏辉 on 4/24/19.
//  Copyright © 2019 Minhui. All rights reserved.
//

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
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
