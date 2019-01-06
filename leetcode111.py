# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        layer = [root]
        k = 0
        while len(layer) != 2**k:
            tmp = []
            for x in layer:
                if x.left ==None:
                    return k+1
                else:
                    tmp.append((x.left))
                if x.right == None:
                    return k+1
                else:
                    tmp.append(x.right)
            layer =tmp
            k+=1
        return k