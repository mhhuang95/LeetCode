class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res =0
        for q in points:
            cmap = {}
            for p in points:
                s = p[0] - q[0]
                f = p[1] - q[1]
                cmap[s**2+f**2] = cmap.get(s**2+f**2,0) + 1
            for k in cmap:
                res += cmap[k]*(cmap[k]-1)
        return res