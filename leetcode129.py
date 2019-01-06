# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        self.findnums(root, 0, nums)
        return sum(nums)

    def findnums(self,root, num, nums):
        if not root:
            return
        num = num*10+root.val
        if root.left == None and root.right == None:
            nums.append(num)
        self.findnums(root.left, num, nums)
        self.findnums(root.right, num, nums)
