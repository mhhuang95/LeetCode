//
// Created by 黄敏辉 on 2019-08-02.
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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        vector<int> path;
        helper(root, res, path, sum);
        return res;
    }

    void helper(TreeNode* root, vector<vector<int>>& res, vector<int>& path, int sum){
        if (root == NULL) return;
        path.push_back(root->val);
        if (!root->left && !root->right && sum == root->val){
            res.push_back(path);
        }
        helper(root->left, res, path, sum - root->val);
        helper(root->right, res, path, sum - root->val);
        path.pop_back();
    }
};