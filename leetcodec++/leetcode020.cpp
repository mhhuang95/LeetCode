//
// Created by 黄敏辉 on 2019-04-26.
//
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValid(string s) {

        stack<char> stack;
        for (int i = 0; i < s.length(); i++){
            if (s[i] == '{' || s[i] == '['||s[i] == '(')
                stack.push(s[i]);
            else if (!stack.empty()
                     && (
                             (s[i] == ')' && stack.top() == '(')
                             || (s[i] == '}' && stack.top() == '{')
                             || (s[i] == ']' && stack.top() == '[')
                     ))
                stack.pop();
            else
                return false;
        }
        return stack.empty();
    }
};