# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = [root.val]
        layer = [root]
        while len(layer) > 0:
            tmp = []
            for x in layer:
                if x.left:
                    tmp.append(x.left)
                if x.right:
                    tmp.append(x.right)
            layer = tmp
            if len(layer) > 0:
                res.append(layer[-1].val)
        return res

    def rightSideView1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        def coll(root, depth):
            if root:
                if depth == len(view):
                    view.append(root.val)
                coll(root.right, depth+1)
                coll(root.left, depth+1)
        coll(root,0)
        return view