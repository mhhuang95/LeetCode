# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(i,j):
            if i > j:
                return None
            mid = (i+j) //2
            root = TreeNode(nums[mid])
            root.left = helper(i,mid-1)
            root.right = helper( mid + 1,j)
            return root
        return helper(0, len(nums)-1)
