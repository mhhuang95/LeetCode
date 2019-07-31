//
// Created by 黄敏辉 on 2019-07-31.
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
    bool isValidBST(TreeNode* root) {
        return valid(root, nullptr, nullptr);
    }

    bool valid(TreeNode* root,  TreeNode* minnode, TreeNode* maxnode){
        if (!root)
            return true;
        if (maxnode && root->val >= maxnode->val || minnode && root->val <= minnode->val)
            return false;
        return valid(root->left, minnode, root) && valid(root->right, root, maxnode);
    }
};