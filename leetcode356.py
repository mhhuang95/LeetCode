class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points = sorted(set(map(tuple,points)))
        return points == sorted((points[0][0]+points[-1][0] -x,y) for x,y in points)

if __name__ == "__main__":
    s = Solution()
    print(s.isReflected([[0,0],[1,0]]))