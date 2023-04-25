from binary_tree import TreeNode


class Solution:
    def rightSideView(self, root):
        output = []

        def recursion_side_view(root, level):
            if not root:
                return None
            if len(output) <= level:
                output.append(root.val)
            recursion_side_view(root.right, level + 1)
            recursion_side_view(root.left, level + 1)

        recursion_side_view(root, 0)
        return output

# https://leetcode.com/submissions/detail/938222887/
