//
// Created by 黄敏辉 on 2019-04-25.
//

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map <char, int> hash = {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500}, {'M',1000}};
        int res = 0;
        int i = 0;
        cout << s.length()<<endl;
        while(i < s.length()){
            if (i > 0 && hash[s[i]] > hash[s[i-1]]){
                res = res + hash[s[i]] - 2*hash[s[i-1]];
            }else
                res = res + hash[s[i]];
            cout << res <<endl;
            i++;
        }
        return res;
    }
};