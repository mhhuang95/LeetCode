# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res):
        if root:
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)
        else:
            res.append(None)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def decode():
            d = next(data)
            if d == None:
                return None
            node = TreeNode(d)
            node.left = decode()
            node.right = decode()
            return node
        return decode()


    def depreorder(self, ):


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))