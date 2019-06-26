//
// Created by 黄敏辉 on 2019-06-26.
//

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.size()<=2)return res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 2; i++){
            int a = nums[i];
            if (a > 0)
                break;
            if (i > 0 && a == nums[i-1])
                continue;
            for (int j = i+1, k = nums.size() - 1; j < k;){
                int b = nums[j];
                int c = nums[k];
                int val = a + b + c;
                if (val == 0) {
                    res.push_back(vector<int>({a, b, c}));
                    while (j<k && b == nums[++j]);
                    while (j < k &&c == nums[--k]);
                } else if (val > 0)
                    k--;
                else
                    j++;
            }
        }
        return res;
    }
};