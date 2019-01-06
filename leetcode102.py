# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        layer = [root]
        res = [[root.val]]
        while len(layer) > 0:
            tmp = []
            for x in layer:
                if x.left:
                    tmp.append(x.left)
                if x.right:
                    tmp.append(x.right)
            layer = tmp
            if len(layer) > 0:
                res.append([x.val for x in layer])
        return res