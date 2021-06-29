"""
解题思路:
N叉树的前序遍历实现根二叉树差不多，唯一不同就是把判断左右子树改成遍历判断children
"""

# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        res = list()
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.children:
                for i in range(len(node.children)-1, -1, -1):
                    stack.append(node.children[i])

        return res

