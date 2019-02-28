# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        root.val = [root.val]
        self.res = 0
        if sum in root.val:
            self.res+=1
        def tra(root):
            if not root:
                return
            if not root.left:
                root.left.val = [x+root.left.val for x in root.val]+[root.left.val]
                if sum in root.left.val:
                    self.res += 1
                tra(root.left)
            if not root.right:
                root.right.val = [x+root.right.val for x in root.val]+[root.right.val]
                if sum in root.right.val:
                    self.res += 1
                tra(root.right)
        tra(root)
        return self.res
