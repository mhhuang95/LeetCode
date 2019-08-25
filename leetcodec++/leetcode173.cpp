//
// Created by 黄敏辉 on 2019-08-25.
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
class BSTIterator {
private:
    stack<TreeNode*> s;
public:
    BSTIterator(TreeNode* root) {
        if (!root)
            return;
        s.push(root);
        TreeNode* tmp = root->left;
        while (tmp){
            s.push(tmp);
            tmp = tmp->left;
        }
    }

    /** @return the next smallest number */
    int next() {
        TreeNode* n = s.top();
        s.pop();
        if (n->right){
            TreeNode* tmp = n->right;
            while (tmp){
                s.push(tmp);
                tmp = tmp->left;
            }
        }
        return n->val;
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }
};