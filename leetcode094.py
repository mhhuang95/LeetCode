# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        self.recursiveTraversal(root, res)
        return res

    def recursiveTraversal(self, root, res):

        if root.left != None:
            self.recursiveTraversal(root.left, res)

        res.append(root.val)
        if root.right != None:
            self.recursiveTraversal(root.right, res)

        return 