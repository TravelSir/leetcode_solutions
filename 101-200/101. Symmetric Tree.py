"""
解题思路:
所谓对称二叉树，即将二叉树的左右子树进行翻转，如果翻转后的左右子树相同，则为对称二叉树
那其实对应到100题，也就是在判断的时候将左子树的左节点和右子树的右节点比较即可
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        p, q = root.left, root.right
        if p == q:
            return True
        if not p or not q:
            return False
        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if p_node.val != q_node.val:
                return False
            if p_node.left and not q_node.right:
                return False
            if not p_node.left and q_node.right:
                return False
            if p_node.right and not q_node.left:
                return False
            if not p_node.right and q_node.left:
                return False
            if p_node.left:
                stack.append((p_node.left, q_node.right))
            if p_node.right:
                stack.append((p_node.right, q_node.left))
        return True
