# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.seperate(inorder, postorder)

    def seperate(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        lp,li = len(postorder), len(inorder)
        root.left = self.seperate(postorder[0:idx], inorder[0:idx])
        root.right = self.seperate(postorder[idx:lp-1], inorder[idx+1:li])
        return root

