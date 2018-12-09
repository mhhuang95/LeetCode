# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def tree(start, end):
            output = []
            for i in range(start,end):
                lefts = tree(start,i)
                rights = tree(i+1,end)
                for l in lefts:
                    for r in rights:
                        root = TreeNode(i)
                        root.left, root.right = l,r
                        output.append(root)
            return output if output else [None]
        return tree(1, n+1)