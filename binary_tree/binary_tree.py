
"""This module contains TreeNode class"""


class TreeNode():
    """_summary_
    Node of binary tree, has:
    val: value of Node
    left: pointer to left Node
    right: pointer to right Node
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
