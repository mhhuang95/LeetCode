# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if key == root.val:
            if root.left and root.right:
                leaf = root.right
                while leaf.left:
                    leaf = leaf.left
                mini = leaf.val
                root.val = mini
                root.right = self.deleteNode(root.right,mini)
            else:
                return root.left or root.right
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

