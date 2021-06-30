"""
解题思路:
要求一个二叉树的最大深度，那其实自顶向下分析，对于根节点来说
f(n) = 1 + max(f(n.left), f(n.right)), 那我们就可以使用递归来实现

这题还有其他解法: 例如直接使用BFS+队列+标记，或使用DFS+栈+标记
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
