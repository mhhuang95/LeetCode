class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        per = 0
        h = len(grid)
        w = len(grid[0])
        extend = [[0]*(w+2)] + [[0] + row + [0] for row in grid] + [[0]*(w+2)]
        for i in range(h+1):
            for j in range(w+1):
                if extend[i][j] != extend[i][j+1]:
                    per += 1
                if extend[i][j] != extend[i+1][j]:
                    per += 1
        return per

if __name__ == "__main__":
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))