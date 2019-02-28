# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def superrob(root):

            if not root:
                return (0,0)
            left, right = superrob(root.left), superrob(root.right)

            rob_now = root.val + left[1]+ right[1]

            rob_later = max(left) + max(right)

            return (rob_now, rob_later)
        return max(superrob(root))