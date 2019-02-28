class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.comb(res,[],n,k,1)
        return res


    def comb(self,res, pre, n,k,start):
        if k == 0:
            res.append(list(pre))
        elif start<=n:
            pre.append(start)
            self.comb(res, pre, n, k-1, start+1)
            pre.pop()
            self.comb(res, pre, n, k, start+1)

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))