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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int >> res;
        vector<TreeNode*> nodes;
        bool flag = true;
        if (!root)
            return res;
        nodes.push_back(root);
        while(!nodes.empty()){
            vector<TreeNode*> tmp;
            vector<int > lel;
            for (int i = 0; i < nodes.size(); i++){
                if (flag)
                    lel.push_back(nodes[i]->val);
                else
                    lel.push_back(nodes[nodes.size()-i-1]->val);
                if (nodes[i]->left)
                    tmp.push_back(nodes[i]->left);
                if (nodes[i]->right)
                    tmp.push_back(nodes[i]->right);

            }
            if (flag)
                flag = false;
            else
                flag = true;
            res.push_back(lel);
            nodes = tmp;
        }
        return res;
    }
};