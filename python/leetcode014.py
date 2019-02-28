class Solution():
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ls = len(strs)
        if ls == 0:
            return ''
        res = strs[0]
        for i in range(1,ls):
            res = self.compare(res, strs[i])
        return res


    def compare(self, res, str):
        m = len(res)
        n = len(str)
        result = ''
        i =0
        while i < m and i < n:
            if res[i] == str[i]:
                result = result + res[i]
                i = i + 1
            else:
                break
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
