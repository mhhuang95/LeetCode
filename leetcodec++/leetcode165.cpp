//
// Created by 黄敏辉 on 2019-08-25.
//

class Solution {
public:
    int compareVersion(string version1, string version2) {
        int l1 = version1.size();
        int l2 = version2.size();
        int v1 = 0, v2 = 0, i = 0 ,j = 0, n = 0, m = 0;

        while (i < l1 || j < l2){
            while (i < l1 && version1[i] != '.') {
                v1 = v1 * 10 + (version1[i] - '0');
                i++;
            }

            while (j < l2 && version2[j] != '.') {
                v2 = v2 * 10 + (version2[j] - '0');
                j++;
            }

            if (v1 > v2)
                return 1;
            if (v1 < v2)
                return -1;

            v1 = v2 = 0;
            i++;
            j++;

        }
        return 0;

    }
};