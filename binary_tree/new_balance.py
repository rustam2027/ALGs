from binary_tree import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        numbers = []

        def get_all(root) -> None:
            if root is not None:
                get_all(root.left)
                numbers.append(root.val)
                get_all(root.right)

        def get_bst(data, left, right) -> TreeNode:
            if left > right:
                return None
            mid = (left + right) // 2
            new = TreeNode(data[mid])
            new.left = get_bst(data, left, mid - 1)
            new.right = get_bst(data, mid + 1, right)
            return new

        get_all(root)

        return get_bst(numbers, 0, len(numbers) - 1)


B = TreeNode(14)
B.left = TreeNode(9)
B.right = TreeNode(16)
B.left.left = TreeNode(2)
B.left.right = TreeNode(13)

A = Solution()
C = A.balanceBST(B)
print()
