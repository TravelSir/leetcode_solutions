"""
解题思路:
1.首先找出从根节点到子节点结束的所有途径
    如何找出所有途径，这里可以采用递归的方式,这里采用的是DFS深度优先遍历
2.在遍历n个子节点时，就有一个长度为n的列表将每一次新遍历到到节点作为路径头，将该新节点的值加入到列表中的所有路径中去

tips:
本来想的是遍历出所有途径，再计算每条途径的结果，但是发现很多子节点共用了一套父节点，导致两条路径上计算出的结果会有重复，
所以这里必须要在遍历的时候就计算，就是这样耗内存


"""
# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.get_path(root, [], sum)
        return self.res

    def get_path(self, node, sum_list, sum):
        if not node:
            return

        tem = copy.copy(sum_list)
        tem.append(0)
        for i in range(len(tem)):
            tem[i] += node.val
            if tem[i] == sum:
                self.res += 1
        if node.left:
            self.get_path(node.left, tem, sum)
        if node.right:
            self.get_path(node.right, tem, sum)
        return


if __name__ == '__main__':
    begin = TreeNode(10)
    s1 = TreeNode(5)
    s2 = TreeNode(-3)
    s3 = TreeNode(3)
    s4 = TreeNode(2)
    s5 = TreeNode(11)
    s6 = TreeNode(3)
    s7 = TreeNode(-2)
    s8 = TreeNode(1)

    begin.left = s1
    begin.right = s2
    s1.left = s3
    s1.right = s4
    s2.right = s5
    s3.left = s6
    s3.right = s7
    s4.right = s8

    sl = Solution()
    print(sl.pathSum(begin, 8))






