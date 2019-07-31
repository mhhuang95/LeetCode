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
    vector<vector<int >> levelOrder(TreeNode* root) {
        vector<vector<int >> res;
        vector<TreeNode*> nodes;
        if (!root)
            return res;
        nodes.push_back(root);
        while(!nodes.empty()){
            vector<TreeNode*> tmp;
            vector<int > lel;
            for (int i = 0; i < nodes.size(); i++){
                lel.push_back(nodes[i]->val);
                if (nodes[i]->left)
                    tmp.push_back(nodes[i]->left);
                if (nodes[i]->right)
                    tmp.push_back(nodes[i]->right);
            }
            res.push_back(lel);
            nodes = tmp;
        }
        return res;
    }
};