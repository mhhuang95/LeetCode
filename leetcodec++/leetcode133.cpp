//
// Created by 黄敏辉 on 2019-08-08.
//

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {}

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
public:
    unordered_map <Node*, Node*> hash;
    Node* cloneGraph(Node* node) {
        if (!node)
            return node;
        if (hash.find(node) == hash.end()){
            hash[node] = new Node(node->val, {});
            for (Node* neighbor: node->neighbors){
                hash[node]->neighbors.push_back(cloneGraph(neighbor));
            }
        }
        return hash[node];
    }
};