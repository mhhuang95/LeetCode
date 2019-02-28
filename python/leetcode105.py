# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.seperate(preorder, inorder)

    def seperate(self, preorder, inorder):
        if preorder == None:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        lp,li = len(preorder), len(inorder)
        root.left = self.seperate(preorder[1:1+idx], inorder[0:idx])
        root.right = self.seperate(preorder[1+idx:lp], inorder[idx+1:li])
        return root

