//
// Created by 黄敏辉 on 2019-08-15.
//

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(res, root);
        return res;
    }
    void helper(vector<int>& res, TreeNode* root){
        if (!root)
            return;
        res.push_back(root->val);
        helper(res, root->left);
        helper(res, root->right);
    }
};