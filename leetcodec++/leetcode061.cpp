//
// Created by 黄敏辉 on 2019-07-18.
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
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode prehead(-1);
        ListNode *n1 = &prehead, *n2 = &prehead;
        int l = 0;

        if(!head)
            return head;

        prehead.next = head;

        while (n1->next){
            l++;
            n1 = n1->next;
        }

        k = k % l;
        n1 = &prehead;

        for (int i = 0; i < k; i++)
            n1 = n1->next;

        while (n1->next){
            n1 = n1->next;
            n2 = n2->next;
        }
        n1->next = prehead.next;
        prehead.next = n2->next;
        n2->next = NULL;

        return prehead.next;
    }
};