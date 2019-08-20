//
// Created by 黄敏辉 on 2019-08-20.
//

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        unordered_map<string, function<int (int, int)>> map = {
                {"+", [](int a, int b){ return a + b;}},
                {"-", [](int a, int b){ return a - b;}},
                {"*", [](int a, int b){ return a * b;}},
                {"/", [](int a, int b){ return a / b;}}
        };
        stack<int> stack;
        for (string& s : tokens){
            if(!map.count(s)){
                stack.push(stoi(s));
            } else{
                int a = stack.top();
                stack.pop();
                int b = stack.top();
                stack.pop();
                stack.push(map[s](b, a));
            }
        }
        return stack.top();
    }
};