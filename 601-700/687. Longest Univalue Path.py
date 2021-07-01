"""
解题思路:
要球最长的同值路径，那么对于一个节点n来说，等于n.val的最长同值路径为 从左子树根节点出发的最长同值单边路径 + 从右子树根节点出发的最长同值单边路径
f(n) = f1(n.left, n.val) + f1(n.right, n.val) + 1
f1(n, val) = max(f1(n.left, val) + f1(n.right, val))   为从根节点出发的最长等值路径
由于肯能在等值路径中，父节点出发的等值路径长度不如子节点的等值路径长度，所以在判断最大路径的时机要选在遍历内部
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        self._max = 0
        stack = [root]

        def dfs(node: TreeNode, val: int) -> int:
            if not node or node.val != val:
                if node:
                    stack.append(node)
                return 0

            left = dfs(node.left, val)
            right = dfs(node.right, val)
            self._max = max(self._max, left + right + 1)
            return max(left, right) + 1

        while stack:
            _node = stack.pop()
            num = dfs(_node.left, _node.val) + dfs(_node.right, _node.val) + 1
            self._max = max(self._max, num)

        return self._max - 1


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(1)
    head.left.left = TreeNode(3)
    head.left.right = TreeNode(3)
    head.right.right = TreeNode(1)

    print(Solution().longestUnivaluePath(head))


