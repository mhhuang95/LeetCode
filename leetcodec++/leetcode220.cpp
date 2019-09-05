//
// Created by 黄敏辉 on 2019-09-04.
//

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        int n = nums.size();
        multiset<int> s;
        for (int i = 0; i <n; i++){
            if (s.size() == k+1){
                auto it = s.find(nums[i-k-1]);
                if (it != s.end())
                    s.erase(it);
            }

            s.insert(nums[i]);

            auto it = s.find(nums[i]);
            if (next(it) != s.end()){
                long long num1 = *(next(it));
                long long num2 = *it;
                if (abs(num1 - num2) <= t)
                {
                    return true;
                }
            }
            if (it != s.begin()){
                long long num1 = *(prev(it));
                long long num2 = *it;
                if (abs(num1 - num2) <= t)
                {
                    return true;
                }
            }
        }
        return false;
    }
};