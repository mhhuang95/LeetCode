# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        t1,t2 = TreeNode(-1),TreeNode(-1)
        if not root:
            return True
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            if root.left != None and root.right != None:
                t1 = root.left
                while t1.right != None:
                    t1 = t1.right
                t2 = root.right
                while t2.left != None:
                    t2 = t2.right
                if t1.val < root.val and t2.val > root.val:
                    return True
                else:
                    return False
            elif root.left != None and root.right == None:
                t1 = root.left
                while t1.right != None:
                    t1 = t1.right
                if t1.val < root.val:
                    return True
                else:
                    return False
            elif root.left == None and root.right != None:
                t2 = root.right
                while t2.left != None:
                    t2 = t2.right
                if t2.val > root.val:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def isValidBST1(self, root):
        res = []
        self.inorder(root,res)

        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True

    def inorder(self,root, res):
        if not root:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
