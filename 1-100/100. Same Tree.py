"""
解题思路：
很简单，就在遍历的时候判断节点所属值是否一致，且是否拥有左右子节点就行了，如果不一致则返回False，无需后续遍历，所以这里可以用栈的方式前序遍历即可
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True
        if not p or not q:
            return False
        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if p_node.val != q_node.val:
                return False
            if p_node.left and not q_node.left:
                return False
            if not p_node.left and q_node.left:
                return False
            if p_node.right and not q_node.right:
                return False
            if not p_node.right and q_node.right:
                return False
            if p_node.left:
                stack.append((p_node.left, q_node.left))
            if p_node.right:
                stack.append((p_node.right, q_node.right))
        return True

