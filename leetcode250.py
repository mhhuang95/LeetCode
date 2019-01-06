# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0

        def helper(root):
            if not root:
                return
            left = helper(root.left)
            right = helper(root.right)
            if (not root.left or left == root.val) and (not root.right or right == root.val):
                count += 1
                return root.val

            return '#'
        helper(root)
        return count
