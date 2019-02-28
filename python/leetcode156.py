# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root and root.left:
            res = self.upsideDownBinaryTree(root.left)
            root.left.right = root
            if root.right:
                root.left.left = root.right
            root.left = None
            root.right = None
            return res
        else:return root