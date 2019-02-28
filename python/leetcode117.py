# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        root.next = None
        layer = [root]
        while len(layer) > 0:
            tmp = []
            for x in layer:
                if x.left != None:
                    tmp.append(x.left)
                if x.right != None:
                    tmp.append(x.right)
            layer = tmp
            if len(layer) > 0:
                for i in range(len(layer)-1):
                    layer[i].next = layer[i+1]
                layer[len(layer)-1].next = None