//
// Created by 黄敏辉 on 2019-07-29.
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
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode prehead(-1);
        prehead.next = head;
        ListNode *tmp = &prehead;
        ListNode *del;
        while (tmp->next){
            if (tmp->next->next && tmp->next->val == tmp->next->next->val){
                while (tmp->next->next && tmp->next->val == tmp->next->next->val){
                    del = tmp->next->next;
                    tmp->next->next = tmp->next->next->next;
                    delete del;
                }
                del = tmp->next;
                tmp->next = tmp->next->next;
                delete del;
                continue;
            }
            tmp = tmp->next;
        }
        return prehead.next;
    }
};