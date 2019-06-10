//
// Created by 黄敏辉 on 2019-06-09.
//

//
// Created by 黄敏辉 on 2019-06-09.
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode prehead(0), *curr = &prehead;
        int carry = 0;
        while (l1 || l2 || carry){
            int sum = (l1? l1->val : 0) + (l2? l2->val : 0) + carry;
            carry = sum / 10;
            curr->next = new ListNode(sum % 10);
            curr = curr->next;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return prehead->next;
    }
};