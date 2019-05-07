//
// Created by 黄敏辉 on 2019-05-07.
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
    bool hasCycle(ListNode *head) {
        if(head == NULL)
            return false;
        ListNode *walker = head;
        ListNode *runner  = head;
        while (runner != NULL && runner->next != NULL){
            runner = runner->next->next;
            walker = walker->next;
            if (walker == runner)
                return true;
        }
        return false;
    }
};