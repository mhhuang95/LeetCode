//
// Created by 黄敏辉 on 2019-08-01.
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }

    TreeNode* helper(vector<int>& preorder, int i, int j, vector<int>& inorder, int k, int l){
        if (i >= j ||k >= j)
            return NULL;

        auto f = find(inorder.begin() + k, inorder.begin() + l, preorder[i]);

        int dis = f - inorder.begin() - k;

        TreeNode* root = new TreeNode(preorder[i]);
        root->left = helper(preorder, i+1, i+1+dis, inorder, k, k+dis);
        root->right = helper(preorder, i+1+dis,j, inorder ,k+dis+1, l);
        return root;
    }
};