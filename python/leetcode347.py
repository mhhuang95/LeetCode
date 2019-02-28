class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for x in nums:
            dic[x] = dic.get(x,0) +1
        res = []
        val_s = sorted(dic.values())[::-1]
        for x in val_s:
            for key in dic:
                if dic[key] == x:
                    res.append(key)
                    dic.pop(key)
                    break

        return res[0:k]