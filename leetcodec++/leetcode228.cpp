//
// Created by 黄敏辉 on 2019-09-06.
//

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        int i = 0;
        while (i < nums.size()){
            int k = i;
            while (i + 1 < nums.size() && nums[i] + 1 == nums[i+1])
                i++;
            res.push_back(to_s(nums[k],nums[i]));
            i++;
        }
        return res;
    }

    string to_s(int i, int j){
        if (i == j)
            return to_string(i);
        else
            return to_string(i) + "->" + to_string(j);
    }
};