# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    class Solution(object):
        def postorderTraversal(self, root):
            stack, res = [root], []
            while stack:
                if stack[-1] != None and (stack[-1].left != None or stack[-1].right != None):
                    stack.append(stack[-1].right)
                    stack.append(stack[-1].left)
                node = stack.pop()
                if node != None:
                    res.append(node.val)
            return res