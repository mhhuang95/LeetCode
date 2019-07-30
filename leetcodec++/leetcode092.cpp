//
// Created by 黄敏辉 on 2019-07-30.
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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode *l,*pre, *tmp1, *tmp2;
        ListNode prehead(-1);
        prehead.next = head;
        l = &prehead;

        for (int i = 0; i < m-1; i++)
            l = l->next;
        pre = l;
        l = l->next;
        tmp1 = l;

        for (int i = 0;i < n-m;i++){
            tmp2 = l->next;
            l->next = l->next->next;
            tmp2->next = tmp1;
            pre->next = tmp2;
            tmp1 = tmp2;
        }

        return prehead.next;

    }
};