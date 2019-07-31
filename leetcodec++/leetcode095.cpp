//
// Created by 黄敏辉 on 2019-07-30.
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
    vector<TreeNode*> generateTrees(int n) {
        if(n==0) return vector<TreeNode*>();
        return genTrees(1,n);

    }
    vector<TreeNode*> genTrees(int f, int k) {
        vector < TreeNode * > res;
        if (f > k)
            res.push_back(0);
        if (f == k)
            res.push_back(new TreeNode(f));
        if (f < k) {
            for (int i = f; i <= k; i++) {

                vector < TreeNode * > l = genTrees(f, i - 1);
                vector < TreeNode * > r = genTrees(i + 1, k);

                for (int j = 0; j < l.size(); j++) {
                    for (int m = 0; m < r.size(); m++) {
                        TreeNode *root = new TreeNode(i);
                        root->left = l[j];
                        root->right = r[m];
                        res.push_back(root);
                    }
                }
            }
        }
        return res;
    }
};