# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q:
            return root

        l = r = None
        if root.left:
            l = self.lowestCommonAncestor(root.left, p,q)
        if root.right:
            r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r