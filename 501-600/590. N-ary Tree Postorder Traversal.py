"""
解题思路:
N叉树的后序遍历实现跟二叉树的后序遍历差不多，把左右子树的判断改成children判断即可
"""

# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        white, red, res = 1, 2, list()
        stack = [(root, white)]

        while stack:
            node, color = stack.pop()
            if color == red:
                res.append(node.val)
                continue

            stack.append((node, red))
            if node.children:
                for i in range(len(node.children) - 1, -1, -1):
                    stack.append((node.children[i], white))

        return res
