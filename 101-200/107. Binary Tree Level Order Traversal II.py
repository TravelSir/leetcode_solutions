"""
解题思路:
这道题直接在原来的二叉树层序遍历的基础上，通过标记节点所在层数，将节点按层数分类成一个列表，每当遍历完一层，
就把这一层的节点列表丢进栈中，最后再把所有数出栈即可


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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = Queue()
        queue.put((root, 1))
        stack, per, per_level = list(), list(), 1

        while not queue.empty():
            node, level = queue.get()
            if per_level != level:
                stack.append(per)
                per = list()
                per_level = level

            per.append(node.val)

            if node.left:
                queue.put((node.left, level + 1))

            if node.right:
                queue.put((node.right, level + 1))

        if per:
            stack.append(per)

        # 用切片来代替出栈的过程
        return stack[::-1]
