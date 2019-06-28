//
// Created by 黄敏辉 on 2019-06-28.
//

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        if (nums.size() < 4)
            return res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 3; i++){
            int a = nums[i];
            if (i > 0 && nums[i-1] == a)
                continue;
            for (int j = i+1; j < nums.size() - 2; j++){
                int b = nums[j];
                if (j > i+1 && nums[j-1] == b)
                    continue;
                int l = j + 1, r = nums.size() - 1;
                while (l < r){
                    int c = nums[l], d = nums[r];
                    int val = a+b+c+d;
                    if (val == target) {
                        res.push_back(vector<int>({a, b, c, d}));
                        do{l++;}while(nums[l]==nums[l-1]&&l<r);
                        do{r--;}while(nums[r]==nums[r+1]&&l<r);
                    }
                    else if(val > target)
                        r--;
                    else
                        l++;
                }
            }
        }
        return res;
    }
};