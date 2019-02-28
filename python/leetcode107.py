# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = [[root.val]]
        layer = [root]
        while len(layer) >0:
            tmp = []
            for x in layer:
                if x.left != None:
                    tmp.append(x.left)
                if x.right != None:
                    tmp.append(x.right)
            layer = tmp
            if len(layer) != 0:
                res.append([l.val for l in layer])
        return res[::-1]