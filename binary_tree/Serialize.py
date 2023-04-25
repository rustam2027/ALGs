from binary_tree import TreeNode


class Codec:

    def serialize(self, root):
        line = "x"
        if root is not None:
            line = str(root.val) + ' '
            line += self.serialize(root.left) + ' '
            line += self.serialize(root.right)
        return line

    def deserialize(self, data):
        data_splited = data.split()

        def recursion_deserialize(arr):
            curr = arr.pop(0)
            if curr == 'x':
                return None

            new = TreeNode(curr)
            new.left = recursion_deserialize(arr)
            new.right = recursion_deserialize(arr)
            return new

        return recursion_deserialize(data_splited)

# https://leetcode.com/submissions/detail/938214440/
