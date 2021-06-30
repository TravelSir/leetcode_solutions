"""
解题思路:
多叉树的层序遍历实现和二叉树的层序遍历实现差不多，使用队列即可
"""
# Definition for a Node.
from queue import Queue
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = Queue()
        queue.put((root, 1))
        res, per, level = [], [], 1
        while not queue.empty():
            node, _level = queue.get()
            if level != _level:
                res.append(per)
                per = []
                level = _level

            per.append(node.val)

            for child in node.children:
                queue.put((child, level + 1))

        if per:
            res.append(per)

        return res

