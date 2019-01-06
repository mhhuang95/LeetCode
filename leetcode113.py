# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        a = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val]+i for i in a]