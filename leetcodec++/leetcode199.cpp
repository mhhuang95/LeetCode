//
// Created by 黄敏辉 on 2019-08-27.
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(!root)
            return res;
        vector<TreeNode*> nodes;
        nodes.push_back(root);
        while(!nodes.empty()){
            vector<TreeNode*> tmp;
            res.push_back(nodes.end()->val)
            for(int i = 0; i < nodes.size(); i++){
                if (nodes[i]->left)
                    tmp.push_back(nodes[i]->left);
                if (nodes[i]->right)
                    tmp.push_back(nodes[i]->right);
            }
            nodes = tmp;
        }
        return res;
    }
};