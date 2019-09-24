//
// Created by 黄敏辉 on 2019-09-24.
//

class Solution {
public:
    bool wordPattern(string pattern, string str) {
        istringstream ss(str);
        string word;
        unordered_map<char, string> m;
        unordered_map<string, char> n;

        for (char c:pattern){
            if(!(getline(ss, word, ' ')))
                return false;
            if ( m.emplace(c,word).first->second != word)
                return false;
            if ( n.emplace(word,c).first->second != c)
                return false;
        }
        return ! getline(ss, word, ' ');

    }
};