//
// Created by 黄敏辉 on 2019-09-03.
//

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> myset;
        for (auto & num:nums){
            if(myset.find(num) != myset.end())
                return true;
            myset.insert(num);
        }
        return false;
    }
};