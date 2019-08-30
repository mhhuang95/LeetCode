//
// Created by 黄敏辉 on 2019-08-27.
//

class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> tmp;

        while(n != 1){
            if (tmp.find(n) == tmp.end()){
                tmp.insert(n);
            } else{
                return false;
            }

            int sum = 0;
            while (n){
                sum += pow(n % 10 ,2);
                n /= 10;
            }

            n = sum;
        }

        return true;
    }
};