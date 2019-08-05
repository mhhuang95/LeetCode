//
// Created by 黄敏辉 on 2019-08-05.
//

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() {}

    Node(int _val, Node* _left, Node* _right, Node* _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* connect(Node* root) {
        Node* t = root;
        helper(t);
        return root;

    }

    void helper(Node* root){
        if (!root)
            return ;
        while (root->left){
            Node* p = root;
            while(p){
                p->left->next = p->right;
                if(p->next)
                    p->right->next = p->next->left;
                p = p->next;
            }
            root = root->left;
        }
    }
};