//
// Created by 黄敏辉 on 2019-04-25.
//
#include <iostream>
#include <unordered_map>
#include <vector>
#include "leetcode001.cpp"
using namespace std;

int main(){
    leetcode001 s;
    vector <int> nums = {2,7,4,9};
    cout << s.twoSum(nums,9)[1]<<endl;
}