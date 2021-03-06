"""
解题思路:
二叉树的中序遍历顺序为: 左子树 根节点 右子树, 左子树和右子树遍历也满足上述顺序
可用递归或栈实现，推荐使用栈实现，防止调用栈溢出
递归的实现为f(n) = f(n.left) + n.val + f(n.right), 要判断left和right是否为空
栈的实现则需要将节点按n.right, n, n.left 的顺序入栈，但会有个问题是如果不加条件，假设取出n，会又添加n.right,n,n.left
所以我们需要增加一个辅助变量来标记节点的左子树是否遍历完了，这样第二次遍历n的时候就直接将n节点的值加入返回值即可
本来是想在节点数据结构中定义一个flag变量的，但leetcode的oj不允许自定义node，所以用一个字典来存储node节点的地址
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = list()
        flag = dict()
        while stack:
            node = stack.pop()

            if flag.get(id(node)):
                res.append(node.val)
                continue

            flag[id(node)] = True
            if node.right:
                stack.append(node.right)

            stack.append(node)

            if node.left:
                stack.append(node.left)

        return res


if __name__ == '__main__':
    head = TreeNode(1)
    head.right = TreeNode(2)
    head.right.left = TreeNode(3)
    print(Solution().inorderTraversal(head))
