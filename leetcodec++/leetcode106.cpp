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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return helper(postorder, 0, postorder.size(), inorder, 0, inorder.size());
    }

    TreeNode* helper(vector<int>& postorder, int i, int j, vector<int>& inorder, int k, int l){
        if (i >= j ||k >= l)
            return NULL;

        auto f = find(inorder.begin() + k, inorder.begin() + l, postorder[j-1]);

        int dis = f - inorder.begin() - k;

        TreeNode* root = new TreeNode(postorder[j-1]);
        root->left = helper(postorder, i, i+dis, inorder, k, k+dis);
        root->right = helper(postorder, i+dis,j-1, inorder ,k+dis+1, l);
        return root;
    }
};