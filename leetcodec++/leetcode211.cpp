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

class WordDictionary {
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new TrieNode();
    }

    /** Adds a word into the data structure. */
    void addWord(string word) {
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

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return search(word.c_str(), root);
    }


private:
    TrieNode* root;

    bool search(const char* word, TrieNode* node) {
        for (int i = 0; word[i] && node; i++) {
            if (word[i] != '.') {
                node = node -> children[word[i] - 'a'];
            } else {
                TrieNode* tmp = node;
                for (int j = 0; j < 26; j++) {
                    node = tmp -> children[j];
                    if (search(word + i + 1, node)) {
                        return true;
                    }
                }
            }
        }
        return node && node -> word;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */