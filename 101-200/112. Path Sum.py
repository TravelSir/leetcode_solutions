"""
解题思路: 典型的DFS, 我们可以自上而下的拆分问题，对于根节点
f(n, num) = f(n.left, num-n.val) or f(n.right, num-n.val)

因为要判断到是到叶子节点，所以当n没有left和right时再判断与n.val与num的值
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            res = targetSum == root.val
        else:
            res = self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        return res


