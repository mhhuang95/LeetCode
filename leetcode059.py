class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        res = [[0]*n for i in range(n)]
        i = 1
        j = 0
        k = 0
        m = 0
        res[k][m] = i
        while i < n*n:
            if j%4 == 0:

                while m+1 < n and res[k][m+1] ==0 :
                    m = m +1
                    i = i + 1
                    res[k][m] = i

                j=j+1
            if j%4 == 1:

                while k+1 < n and res[k+1][m] == 0:
                    k = k + 1
                    i = i + 1
                    res[k][m] = i

                j = j + 1
            if j % 4 == 2:

                while m-1>=0 and res[k][m -1] == 0:
                    m = m - 1
                    i = i + 1
                    res[k][m] = i

                j = j + 1
            if j % 4 == 3:

                while k-1>=0 and res[k-1][m] == 0:
                    k = k -1
                    i = i + 1
                    res[k][m] = i

                j = j + 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix(3))