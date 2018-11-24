class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            for j in reversed(range(len(res))):
                res.append(res[j] + (1 << i))
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.grayCode(3))