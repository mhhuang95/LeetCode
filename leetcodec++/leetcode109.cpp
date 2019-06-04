//
// Created by 黄敏辉 on 2019-05-15.
//

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    static int length(const ListNode* node){
        int res = 0;
        while(node){
            res ++;
            node = node->next;
        }
        return res;
    }

    TreeNode* create(ListNode*& cur, int count){
        const int count_l = count/2;
        const int count_r = count - count_l - 1;
        auto node = new TreeNode(0);
        if (count_l > 0)
            node->left = create(cur, count_l);
        node->val = cur->val;
        cur = cur->next;
        if (count_r > 0)
            node->right = create(cur, count_r);
        return node;
    }


public:
    TreeNode* sortedListToBST(ListNode* head) {
        const int len = length(head);
        return (len > 0) ? create(head, len) : nullptr;
    }
};