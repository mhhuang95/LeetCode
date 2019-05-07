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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *a = headA;
        ListNode *b = headB;

        int la = 0;
        while (a != NULL){
            la ++;
            a = a->next;
        }

        int lb = 0;
        while (b != NULL){
            lb ++;
            b = b->next;
        }

        if (la > lb){
            for (int i = 0; i < (la-lb); i++){
                headA = headA->next;
            }
        }

        if (la < lb){
            for (int i = 0; i < (lb-la); i++){
                headB = headB->next;
            }
        }



        while(headA){
            if (headA == headB)
                return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* tmp_head = headB;
        while (headA != NULL){
            while (tmp_head != NULL){
                if (tmp_head == headA)
                    return headA;
                tmp_head = tmp_head->next;
            }
            headA = headA->next;
            tmp_head = headB;
        }
        return NULL;
    }
};