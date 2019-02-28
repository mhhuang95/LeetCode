# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return
        self.res = root.val
        def helper(root):
            if not root:
                return
            if abs(target-root.val) < abs(target-self.res):
                self.res = root.val
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.res