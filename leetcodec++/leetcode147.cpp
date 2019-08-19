//
// Created by 黄敏辉 on 2019-08-19.
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
    ListNode* insertionSortList(ListNode* head) {
        if (!head || !head->next)
            return head;
        ListNode* prehead = new ListNode(-1);
        prehead->next = head;
        ListNode *p, *q, *r, *t;
        int k = 1;
        bool flag = false;

        p = head;
        q = head->next;


        while (q){
            t = prehead;
            r = q;
            q = q->next;
            p->next = q;
            flag = false;
            for (int i = 0; i < k; i++){
                if (r->val <= t->next->val){
                    r->next = t->next;
                    t->next = r;
                    flag = true;
                    break;
                }
                t = t->next;
            }
            if (!flag){
                r->next = t->next;
                t->next = r;
            }
            k++;
            p = prehead;
            for (int i = 0; i < k; i++){
                p = p->next;
            }
        }

        return prehead->next;
    }
};