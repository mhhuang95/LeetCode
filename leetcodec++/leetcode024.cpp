//
// Created by 黄敏辉 on 2019-06-29.
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
    ListNode* swapPairs(ListNode* head) {
        ListNode prehead(-1);
        prehead.next = head;

        ListNode *tmp1 = &prehead, *tmp2;

        while (tmp1->next && tmp1->next->next){
            tmp2 = tmp1->next;
            tmp1->next = tmp1->next->next;
            tmp2->next = tmp1->next->next;
            tmp1->next->next = tmp2;
            tmp1 = tmp1->next->next;
        }

        return prehead.next;
    }
};