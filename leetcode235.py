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
        if root == q or root == q:
            return root

        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p,q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p,q)

        if left and right:
            return root
        else:return left or right


class Solution1:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val > max(q.val, p.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(q.val, p.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root