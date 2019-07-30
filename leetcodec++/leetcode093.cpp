//
// Created by 黄敏辉 on 2019-07-30.
//

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        int i,j,k,l;
        for (i = 1;i < 4;i++){
            for (j = i+1; j < i+4;j++){
                for (k = j+1; k < j+4; k++){
                    l = s.length() - k;
                    if (l > 3 || l < 1)
                        continue;
                    if (isValid(s.substr(0,i)) && isValid(s.substr(i,j-i)) && isValid(s.substr(j,k-j)) &&isValid(s.substr(k,l)) )
                        res.push_back(s.substr(0,i)+'.'+s.substr(i,j-i)+'.'+s.substr(j,k-j)+'.'+s.substr(k,l));
                }
            }
        }
        return res;

    }

    bool isValid(string num){
        if (num[0] == '0' && num.length() > 1)
            return false;
        int res=0;
        for (int i=0; i<num.size(); i++)
            res = 10*res + num[i]-'0';
        if (res >=0 && res <= 255)
            return true;
        return false;
    }
};