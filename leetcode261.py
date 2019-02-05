class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        neighbor = {i: [] for i in range(n)}
        for v,w in edges:
            neighbor[v] += w,
            neighbor[w] += v,
        def visit(v):
            l = neighbor.pop(v, [])
            for w in l:
                visit(w)
        visit(0)
        return not neighbor


if __name__ == "__main__":
    s = Solution()
    print(s.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))
