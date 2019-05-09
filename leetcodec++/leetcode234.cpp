//
// Created by 黄敏辉 on 2019-05-09.
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
    ListNode* temp;
    bool isPalindrome(ListNode* head) {
        temp = head;
        return check(head);
    }

    bool check(ListNode* p){
        if (p == NULL)
            return true;
        bool ispal = check(p->next) && (temp->val == p->val);
        temp = temp->next;
        return ispal;
    }
};