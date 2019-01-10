# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        col = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                col[i].append(node.val)
                queue += (node.left, i-1), (node.right, i+1)

        return [col[i] for i in sorted(col)]