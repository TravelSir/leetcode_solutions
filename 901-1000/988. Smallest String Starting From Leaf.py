"""
解题思路:
分析题目得出，我们需要遍历到所有叶子节点，且找出叶子节点到根节点到最小字符串
那么首先在我们使用DFS遍历到叶子节点到时候，得有一个空间存储从根节点到该叶子节点前的节点，由于需要倒叙，所以我们用递归+栈来遍历和存
我们需要找出最小字符串，那么我们就需要一个中间最小字符串来和每一次遍历到叶子节点时组成到倒叙字符串比较，若倒叙字符串更小，则取代最小字符串
这样只有一个变量，就能在一次遍历中找出最小字符串
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""

        self.min_list, stack = [], []

        def dfs(node: TreeNode):
            stack.append(node.val)
            if not node.left and not node.right:
                self.min_list = self.get_min(stack[::-1], self.min_list)

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()
        dfs(root)
        return "".join([chr(ord('a')+i)for i in self.min_list])

    @staticmethod
    def get_min(node_list: List[int], min_list: List[int]) -> List[int]:
        if not min_list:
            return node_list

        for i in range(len(min_list)):
            if i >= len(node_list):
                return node_list
            if min_list[i] < node_list[i]:
                return min_list
            elif min_list[i] > node_list[i]:
                return node_list

        return min_list
