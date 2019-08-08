//
// Created by 黄敏辉 on 2019-08-08.
//
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> path;

        findPartition(0, s, res, path);
        return res;
    }

    void findPartition(int index, string s, vector<vector<string>>& res, vector<string> path){
        if(index == s.size()){
            res.push_back(path);
            return;
        }
        for (int i = index; i < s.size(); i++){
            if (isPalindrome(s, index, i)){
                path.push_back(s.substr(index, i-index + 1));
                findPartition(i+1, s, res, path);
                path.pop_back();
            }
        }
    }

    bool isPalindrome(const string& s, int start, int end){
        while(start <= end) {
            if (s[start++] != s[end--]) {
                return false;
            }
        }
        return true;
    }
};