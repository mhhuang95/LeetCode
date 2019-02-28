class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        p = [[1 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        tag = 0
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                tag = 1
            if tag == 1:
                p[i][0] = 0
        tag = 0
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                tag = 1
            if tag == 1:
                p[0][j] = 0


        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    p[i][j] = p[i - 1][j] + p[i][j - 1]
                else:
                    p[i][j] = 0
        return p[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[0],[1]]))