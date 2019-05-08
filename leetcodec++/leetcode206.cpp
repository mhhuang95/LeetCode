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
    ListNode* reverseList(ListNode* head) {
        if (head == NULL){
            return head;
        }
        ListNode* res = new ListNode(0);
        ListNode* tmp;
        while (head != NULL){
            tmp = head;
            cout << tmp->val<<endl;
            head = head->next;
            tmp->next = res->next;
            res->next = tmp;
        }
        return res->next;
    }
};

