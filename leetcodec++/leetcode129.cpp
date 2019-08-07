//
// Created by 黄敏辉 on 2019-08-07.
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
    int sumNumbers(TreeNode* root) {
        vector<int> nums;
        findNums(nums, root);
        int res = 0;
        for (int i = 0; i < nums.size(); i++)
            res += nums[i];
        return res;
    }

    void findNums(vector<int>& nums, TreeNode* root){
        if (!root)
            return;
        if (!root->left && !root->right){
            nums.push_back(root->val);
            return;
        }
        if (root->left){
            root->left->val = root->val * 10 + root->left->val;
        }
        findNums(nums, root->left);
        if (root->right){
            root->right->val = root->val * 10 + root->right->val;
        }
        findNums(nums, root->right);

        return;
    }
};