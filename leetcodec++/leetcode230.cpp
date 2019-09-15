//
// Created by 黄敏辉 on 2019-09-15.
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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> sorted_elements;
        in_tra(root, sorted_elements);
        return sorted_elements[k-1];
    }

    void in_tra(TreeNode* root, vector<int>& sorted_elements){
        if (root->left){
            in_tra(root->left, sorted_elements);
        }
        sorted_elements.push_back(root->val);
        if (root->right){
            in_tra(root->right, sorted_elements);
        }
    }
};