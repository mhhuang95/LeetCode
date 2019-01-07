# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def markleaves(root, l):
            if (not root.left or root.left.val == '#') and(not root.right or root.right.val == '#'):
                l.append(root.val)
                root.val = '#'
            if root.left and root.left.val != '#':
                markleaves(root.left, l)
            if root.right and root.right.val != '#':
                markleaves(root.right, l)

        p = root
        res = []
        while not p and p.val!="#":
            l = []
            markleaves(p,l)
            res.append(l)
            p = root
        return res
