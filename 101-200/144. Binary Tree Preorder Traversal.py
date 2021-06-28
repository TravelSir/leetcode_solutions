"""
解题思路:
二叉树的前序遍历顺序为: 根节点 左子树 右子树, 左子树和右子树遍历也满足上述顺序
可用递归或栈实现，推荐使用栈实现，防止调用栈溢出
递归的实现为f(n) = n.val + f(n.left) + f(n.right), 要判断left和right是否为空
栈的实现其实就是用数组将当前节点的值记录，然后再需要计算的right和left依次进入数组，循环遍历数组，每次取栈尾节点出来计算，直到数组为空
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = list()
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

