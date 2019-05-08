//
// Created by 黄敏辉 on 2019-05-08.
//

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* res;
        ListNode* tmp = NULL;
        res = tmp;
        while (head != NULL){
            if (head->val != val && res == NULL){
                res = new ListNode(head->val);
                tmp = res;
            }else if (head->val != val){
                tmp->next = new ListNode(head->val);
                tmp = tmp->next;
            }
            head = head->next;
        }
        return res;
    }
};