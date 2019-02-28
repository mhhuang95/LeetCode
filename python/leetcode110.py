# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root == None:
                return 0
            l = check(root.left)
            r = check(root.right)
            if l == -1 or r == -1 or abs(r-l) > 1:
                return -1
            return 1+max(l,r)

        return check(root) != -1