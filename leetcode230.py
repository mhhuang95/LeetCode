# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nums = []
        self.inordertra(root, nums)
        return nums[k-1]

    def inordertra(self, root, res):
        if not root:
            return
        self.inordertra(root.left, res)
        res.append(root.val)
        self.inordertra(root.right,res)