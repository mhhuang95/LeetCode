//
// Created by 黄敏辉 on 2019-07-19.
//
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> dirs;
        string result ="";
        for(auto i= path.begin();i!=path.end();i++)
        {
            auto j = find(i,path.end(),'/');  //返回一个iterator;若不存在，则会返回一个end()指针
            string str = string(i,j);  //i=j时则为空
            if(str.empty() || str==".") continue;
            if(str==".."){
                if(!dirs.empty())
                    dirs.pop_back();}
            else
                dirs.push_back(str);

            i=j;
            if(i==path.end()) break; //对应j=end()指针，比如"/a/.."会出现这种情况
        }

        if(dirs.size()==0)  return "/";
        for(int i=0; i<dirs.size();i++)
        {
            result += "/" + dirs[i];
        }

        return result;
    }
};