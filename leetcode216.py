class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def helper(i,k,n,res,seq):
            if i == 10:
                if k == 0 and n == 0:
                    res.append(seq)
                return 

            if n >= i and k > 0:
                helper(i+1,k-1,n-i,res,seq+[i])

            helper(i+1,k,n,res,seq)

        res = []
        helper(1,k,n,res,[])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3,7))
