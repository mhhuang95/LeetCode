# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        res = []
        self.inordertra(root, res)
        for i in range(len(res)):
            if res[i].val == p.val:
                if i < len(res):
                    return res[i+1]
                else:
                    return None

    def inordertra(self, root, res):
        if not root:
            return
        self.inordertra(root.left, res)
        res.append(root)
        self.inordertra(root.right,res)

class Solution1(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        succ = None
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            else:
                root = root.right

        return succ