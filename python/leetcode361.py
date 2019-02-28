class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        max_kill = 0
        if len(grid) == 0:
            return 0
        m,n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            row_hit = 0
            for j in range(n):
                if grid[i][j] == 'W':
                    row_hit = 0
                elif grid[i][j] == 'E':
                    row_hit += 1
                else:
                    dp[i][j] += row_hit

        for i in range(m):
            row_hit = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 'W':
                    row_hit = 0
                elif grid[i][j] == 'E':
                    row_hit += 1
                else:
                    dp[i][j] += row_hit

        for j in range(n):
            col_hit = 0
            for i in range(m):
                if grid[i][j] == 'W':
                    col_hit = 0
                elif grid[i][j] == 'E':
                    col_hit += 1
                else:
                    dp[i][j] += col_hit

        for j in range(n):
            col_hit = 0
            for i in range(m-1, -1,-1):
                if grid[i][j] == 'W':
                    col_hit = 0
                elif grid[i][j] == 'E':
                    col_hit += 1
                else:
                    dp[i][j] += col_hit
                    max_kill = max(max_kill, dp[i][j])

        return max_kill