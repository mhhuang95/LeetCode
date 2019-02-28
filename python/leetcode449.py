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
        self.res = ''

        def tra(root):
            if root:
                self.res += str(root.val) + '_'
                tra(root.left)
                tra(root.right)

        tra(root)
        return self.res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        val = [int(x) for x in data.split('_')]

        def buildtree(val):
            if len(val) == 0:
                return None
            root = TreeNode(val[0])
            i = 1
            while i < len(val) and val[i] <= val[0]:
                i += 1
            root.left = buildtree(val[1:i])
            root.right = buildtree(val[i:])
            return root

        return buildtree(val)


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    s = Codec()
    l = s.deserialize('2_1_3')



        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))