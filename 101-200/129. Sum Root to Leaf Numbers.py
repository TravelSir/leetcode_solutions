"""
解题思路:
这题其实很简单，前序遍历，但使用栈 + 标记法，将计算后的值一直带到叶子节点即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 0)]
        _sum = 0

        while stack:
            node, val = stack.pop()

            val = val * 10 + node.val

            if not node.left and not node.right:
                _sum += val

            if node.left:
                stack.append((node.left, val))

            if node.right:
                stack.append((node.right, val))

        return _sum
