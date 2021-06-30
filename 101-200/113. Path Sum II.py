"""
解题思路:
要找出所有路径，就得遍历完所有叶子节点。就需要DFS递归节点，再用一个数组记录从根节点到当前节点的路径
"""
# Definition for a binary tree node.
import copy
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        path = []

        def dfs(node: TreeNode, num: int):
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == num:
                    res.append(path[:])
            else:
                if node.left:
                    dfs(node.left, num - node.val)
                if node.right:
                    dfs(node.right, num - node.val)
            path.pop()

        dfs(root, targetSum)
        return res
