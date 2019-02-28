# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        tmp = str(root.val)
        def paths(root, tmp, res):
            if not root.left and not root.right:
                res.append(tmp)
            if root.left:
                paths(root.left, tmp+'->'+str(root.left.val),res)
            if root.right:
                paths(root.right, tmp + '->' + str(root.right.val), res)
        paths(root, tmp, res)
        return res