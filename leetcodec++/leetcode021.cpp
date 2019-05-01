//
// Created by 黄敏辉 on 2019-04-30.
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* head = NULL;
        ListNode* p = NULL;
        while (l1!= NULL && l2!=NULL){
            printf("%d, %d\n", l1->val, l2->val);
            if (l1->val < l2->val) {
                if (head == NULL){
                    head = p = l1;
                    l1 = l1->next;
                }else{
                    p->next = l1;
                    p = p->next;
                    l1 = l1->next;
                }

            }
            else {
                if (head == NULL){
                    head = p = l2;
                    l2 = l2->next;
                }else{
                    p->next = l2;
                    p = p->next;
                    l2 = l2->next;
                }

            }
        }
        if (l1){
            if (head == NULL)
                head = l1;
            else
                p->next = l1;
        }
        if (l2){
            if (head == NULL)
                head = l2;
            else
                p->next = l2;
        }
        return head;
    }
};