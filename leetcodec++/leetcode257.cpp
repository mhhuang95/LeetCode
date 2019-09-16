//
// Created by 黄敏辉 on 2019-09-16.
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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        if (!root)
            return res;
        findpaths(res, root, to_string(root->val));
        return res;
    }

    void findpaths(vector<string>& res,  TreeNode* root, string t){
        if (!root->left && !root->right) {
            res.push_back(t);
            return;
        }
        if (root->left)
            findpaths(res, root->left, t + "->" + to_string(root->left->val));
        if (root->right)
            findpaths(res, root->right, t + "->" + to_string(root->right->val));

    }
};