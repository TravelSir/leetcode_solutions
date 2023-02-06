"""
解题思路: 一道简单的DFS题目，由于我们确定一个节点的值需要判断是否有子节点，所以这里用后序遍历的方式来做，用递归来实现最易懂。
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        result = self.end_traverse(root)
        return True if result else False

    def end_traverse(self, node, result=None):
        if node.left:
            left = self.end_traverse(node.left, result)
        if node.right:
            right = self.end_traverse(node.right, result)
        if node.left:
            result = self.calculate(node.val, left, right)
        else:
            result = node.val
        return result

    def calculate(self, op, left, right):
        if op == 2:
            return left or right
        else:
            return left and right


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    print(Solution().evaluateTree(root))
