//
// Created by 黄敏辉 on 2019-08-20.
//

class Solution {
public:
    void reverse(string& s, int i, int j){
        while(i < j){
            char t = s[i];
            s[i++] = s[j];
            s[j--] = t;
        }
    }

    string reverseWords(string s) {
        int i = 0, j =0,  l= 0;
        int len = s.size();
        int word = 0;

        while (true){
            while (s[i] == ' ') i++;
            if (i == len) break;
            if (word)
                s[j++] = ' ';
            l = j;
            while (i < len && s[i] != ' '){
                s[j] = s[i];
                i++;
                j++;
            }
            reverse(s, l, j-1);
            word++;
        }

        s.resize(j);
        reverse(s, 0, j-1);
        return s;
    }
};