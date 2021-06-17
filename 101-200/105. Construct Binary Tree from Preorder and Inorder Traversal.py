"""
解题思路：
前序遍历的顺序是根，左，右。
中序遍历的顺序是左，根，右。

由动态规划的思想:
前序: dp(根) = 根 + dp(左) + dp(右)
中序: dp(根) = dp(左) + 根 + dp(右)

其中 中序遍历中的dp(左)和dp(右) 由根节点的位置决定可以划分出来
但 前序遍历中但dp(左)和dp(右) 的边界不清楚

所以重点在于从中序遍历中找出前序遍历的左右子树临界点
其实很简单，因为一个树的中序遍历和前序遍历的长度是一样的，
所以
    前序长度: 1(根节点) + len(左子树前序) + len(右子树前序)
    中序长度: len(左子树中序) + 1(根节点) + len(右子树中序)
    其中len(左子树前序) = len(左子树中序)
    所以中序遍历中根节点的位置等于前序遍历中左子树最后一个点的位置

"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = preorder[0]
        head = TreeNode(root)

        if len(preorder) == 1:
            return head

        stack = list()
        stack.append((preorder, inorder, head))

        while stack:
            _preorder, _inorder, _head = stack.pop()

            if len(_preorder) <= 1:
                continue

            # 找出中序遍历中的根节点，区分左右子树, 同时也是左子树长度
            in_root = _inorder.index(_preorder[0])

            # 说明有左子树
            if in_root > 0:
                _left = TreeNode(_preorder[1])
                _head.left = _left

                left_preorder = _preorder[1: in_root+1]
                left_inorder = _inorder[:in_root]

                stack.append((left_preorder, left_inorder, _left))
                # 说明有右子树
                if in_root < len(_preorder) - 1:
                    _right = TreeNode(_preorder[in_root+1])
                    _head.right = _right

                    right_preorder = _preorder[in_root+1:]
                    right_inorder = _inorder[in_root+1:]
                    stack.append((right_preorder, right_inorder, _right))

            else:
                _right = TreeNode(_preorder[1])
                _head.right = _right
                _preorder = _preorder[1:]
                _inorder = _inorder[1:]

                stack.append((_preorder, _inorder, _right))

        return head


if __name__ == '__main__':
    _head = Solution().buildTree([1,2,3], [3,2,1])
    print(_head)

