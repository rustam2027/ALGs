from binary_tree import TreeNode


class Solution:
    def isValidBST(self, root):
        def recursion(root, interval: tuple):
            left, right = interval
            if left >= root.val or root.val >= right:
                return False
            ret = True

            if root.left:
                ret = ret and recursion(root.left, (left, root.val))
            if root.right:
                ret = ret and recursion(root.right, (root.val, right))
            return ret

        if not root:
            return True

        return recursion(root, (-float('inf'), float('inf')))

# https://leetcode.com/submissions/detail/938234273/
