"""
解题思路:
二叉树的层序遍历也就是BFS广度优先算法。
层序遍历的顺序是: 从左往右遍历每一层的节点
需从左往右访问所有节点。若以单一节点为主，回溯过程太长太复杂。所以BFS与队列的特性非常吻合。
这题还要求把每一层的节点分类，所以采用标记法标记节点的层数
"""


# Definition for a binary tree node.
from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = Queue()
        queue.put((root, 1))
        res, per, per_level = list(), list(), 1

        while not queue.empty():
            node, level = queue.get()
            if per_level != level:
                res.append(per)
                per = list()
                per_level = level

            per.append(node.val)

            if node.left:
                queue.put((node.left, level+1))

            if node.right:
                queue.put((node.right, level+1))

        if per:
            res.append(per)

        return res

