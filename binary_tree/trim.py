from binary_tree import TreeNode


class Solution:
    def trimBST(self, root, low: int, high: int):
        if not root:
            return None

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if root.val < low:
            return root.right
        elif root.val > high:
            return root.left
        else:
            return root

# https://leetcode.com/problems/trim-a-binary-search-tree/submissions/939339403/
