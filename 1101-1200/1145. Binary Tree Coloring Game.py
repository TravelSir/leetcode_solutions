"""
解题思路:
注意: 相邻节点的定义为同一父节点下的左右子节点为相邻节点。而不是同一层级的子节点都算相邻。
那么一个节点只有三种走法，一是往父节点染色，一是往子节点染色，一是往邻节点染色。
那么假如A选择了某个节点n，为了获胜B只能选择A的三个能染色节点去封堵A。
1。那么B若选择节点n的父节点m，那就标识A选不到m节点的父节点的另一子树的所有节点。
那么A必定下一个点就会选择m节点的另一子节点同时也是n的邻节点，让A选不到m节点下的所有子节点。
那么其实这个时候比较的就是m节点下所有子节点树是否大于n/2，大于则B输
2。那么B若选择节点n的邻节点l，那么A选择不到l下的所有子节点的情况下肯定会选择父节点m。
那么这个时候则判断节点l及l节点下的所有子节点树是否大于n/2，大于则B赢
3。若B选择n的子节点(k或j)，那么A必定会选择n的另一子节点。
那么这个时候判断k节点及k节点下的所有子节点树是否大于n/2，大于则B赢

这三种情况符合其一B都能赢
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        parent, node = self.find_node(root, x)
        if parent:
            if self.count_node(node) < n/2:
                return True
            other_node = parent.right if parent.left == node else parent.left
            if other_node and self.count_node(other_node) > n/2:
                return True

        if node.left and self.count_node(node.left) > n/2:
            return True

        if node.right and self.count_node(node.right) > n/2:
            return True

        return False

    def find_node(self, node, x):
        stack = [node]
        parent = [None]
        while stack:
            _node = stack.pop()
            _parent = parent.pop()
            if _node.val == x:
                return _parent, _node
            if _node.right:
                stack.append(_node.right)
                parent.append(_node)
            if _node.left:
                stack.append(_node.left)
                parent.append(_node)
        return None, None

    def count_node(self, node):
        result = list()
        stack = [node]
        while stack:
            _node = stack.pop()
            result.append(_node.val)
            if _node.right:
                stack.append(_node.right)
            if _node.left:
                stack.append(_node.left)
        return len(result)


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    # head.right.left = TreeNode(6)
    # head.right.right = TreeNode(7)
    # head.left.left.left = TreeNode(8)
    # head.left.left.right = TreeNode(9)
    # head.left.right.left = TreeNode(10)
    print(Solution().btreeGameWinningMove(head, 5, 2))

