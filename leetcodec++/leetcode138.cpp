//
// Created by 黄敏辉 on 2019-08-12.
//

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> hash;
        Node* t = head;
        while(t){
            Node* tmp = new Node(t->val, NULL, NULL);
            hash.insert({t, tmp});
            t = t->next;
        }
        t = head;
        while(t){
            hash[t]->next = hash[t->next];
            hash[t]->random = hash[t->random];
            t = t->next;
        }
        return hash[head];
    }
};