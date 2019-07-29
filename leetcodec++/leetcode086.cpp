//
// Created by 黄敏辉 on 2019-07-29.
//

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode prehead(-1);
        prehead.next = head;
        ListNode* p, *q, *tmp;
        p = &prehead;
        while (p->next && p->next->val < x)
            p = p->next;
        q = p;
        while (q && q->next){
            if (q->next->val < x){
                tmp = q->next;
                q->next = q->next->next;
                tmp->next = p->next;
                p->next = tmp;
                p = p->next;
                continue;
            }
            q = q->next;
        }
        return prehead.next;
    }
};