//
// Created by 黄敏辉 on 2019-09-02.
//

class TrieNode{
public:
    TrieNode(bool end=false){
        memset(branches, 0, sizeof(branches));
        isEnd = end;
    }
    TrieNode* branches[26];
    bool isEnd;
};

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* node = root;
        int i;
        for(i = 0; i < word.size(); i++){
            if (node->branches[word[i] - 'a'] == NULL)
                break;
            else{
                node = node->branches[word[i] - 'a'];
                node->isEnd=((i==word.size()-1)?true:node->isEnd);
            }
        }
        for (; i < word.size(); i++){
            node->branches[word[i] - 'a'] = new TrieNode(i==word.size()-1);
            node=node->branches[word[i]-'a'];
        }
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* node = root;
        int i;
        for(i = 0; i < word.size(); i++){
            if(node->branches[word[i] - 'a'] == NULL)
                return false;
            else {
                node = node->branches[word[i] - 'a'];
            }

        }
        return node->isEnd;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* node = root;
        int i;
        for(i = 0; i < prefix.size(); i++){
            if(node->branches[prefix[i] - 'a'] == NULL)
                return false;
            else {
                node = node->branches[prefix[i] - 'a'];
            }

        }
        return true;
    }

private:
    TrieNode* root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */