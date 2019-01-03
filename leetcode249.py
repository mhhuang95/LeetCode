class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        diffs = []
        for s in strings:
            diff=""
            ls = len(s)
            for i in range(1,ls):
                diff.append(str((ord(s[i]) - ord(s[i-1]))%26) + ' ')
            diffs.append(diff)
        res = {}
        l = len(strings)
        for i in range(l):
            if diffs[i] not in res:
                res[diffs[i]] = [strings[i]]
            else:
                res[diffs[i]].append(strings[i])
        return list(res.values())
