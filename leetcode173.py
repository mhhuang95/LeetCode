# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

# @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

# @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val



            # Your BSTIterator object will be instantiated and called as such:
            # obj = BSTIterator(root)
            # param_1 = obj.next()
            # param_2 = obj.hasNext()