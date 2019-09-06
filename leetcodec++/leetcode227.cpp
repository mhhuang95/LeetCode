//
// Created by 黄敏辉 on 2019-09-05.
//

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int calculate(string s) {
        stack<int> nums;
        int res = 0;
        int num = 0;
        char sign = '+';
        for(int i = 0; i < s.size(); i++){
            if (isdigit(s[i])){
                num = num * 10 + s[i] - '0';
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.size() - 1){
                if (sign == '-')
                    nums.push(-num);
                else if (sign == '+')
                    nums.push(num);
                else{
                    int tmp;
                    if (sign == '*')
                        tmp = nums.top() * num;
                    else
                        tmp = nums.top() / num;
                    nums.pop();
                    nums.push(tmp);
                }
                sign = s[i];
                num = 0;
            }
        }
        while(!empty(nums)){
            res += nums.top();
            nums.pop();
        }
        return res;
    }
};