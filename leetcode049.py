class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs.sort()
        hash = {}
        for s in strs:
            key = self.get_keys(s)
            try:
                hash[key].append(s)
            except:
                hash[key] = [s]
        return list(hash.values())

    def get_keys(self,s):
        table = [0] *26
        for x in s:
            table[ord(x) - ord('a')] += 1
        return str(table)

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))