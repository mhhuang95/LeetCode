//
// Created by 黄敏辉 on 2019-07-22.
//


class Solution {
public:
    bool searchMatrix(vector<vector<int> >& matrix, int target)
    {
        int m = matrix.size();
        if (!m) return false;
        int n = matrix[0].size();
        if (!n) return false;

        int l=-1, r=m*n-1;
        while(r-l>1)
        {
            int mid = l + (r-l)/2;
            if (matrix[mid/n][mid%n]==target) return true;
            else if (matrix[mid/n][mid%n]>target) r=mid;
            else l=mid;
        }
        if (matrix[r/n][r%n]==target) return true;
        else return false;
    }
};