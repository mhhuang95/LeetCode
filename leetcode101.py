# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.ismirror(root.left, root.right)

    def ismirror(self,left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            return self.ismirror(left.left, right.right) and self.ismirror(left.right, right.left)
        else:
            return False