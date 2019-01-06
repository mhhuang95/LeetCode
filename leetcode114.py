# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        l = []
        def preTraversal(root,res):
            if not root:
                return []
            else:
                res.append(root)
            if root.left != None:
                preTraversal(root.left, res)
            if root.right != None:
                preTraversal(root.right, res)
        preTraversal(root,l)
        r = l[0]
        l[0].left = None
        for i in range(1, len(l)):
            r.left = None
            r.right = l[i]
            r = l[i]
        r.right = None
        r.left = None
        return l[0]
