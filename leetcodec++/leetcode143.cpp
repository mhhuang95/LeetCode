//
// Created by 黄敏辉 on 2019-08-14.
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
    void reorderList(ListNode* head) {
        if (head == NULL || head->next == NULL || head->next->next == NULL)
            return;

        ListNode *p = head, *q = head;

        while (p && q && q->next && q->next->next){
            p = p->next;
            q = q->next->next;
        }

        ListNode *mid = p->next;
        p->next = NULL;
        p = head;

        ListNode *q1=mid, *q2,*q3;
        if (mid->next){
            q1 = mid;
            q2 = mid->next;
            while (q2){
                q3 = q2->next;
                q2->next = q1;
                q1 = q2;
                q2 = q3;
            }
            mid->next = NULL;
        }
        q = q1;

        ListNode *s=p;
        p=p->next;
        while(p && q){
            s->next = q;
            s = s->next;
            q = q->next;

            s->next = p;
            s = s->next;
            p = p->next;
        }
        if (q)
            s->next = q;
        if (p)
            s->next = p;
    }
};