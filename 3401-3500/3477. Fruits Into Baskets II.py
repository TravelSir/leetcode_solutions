"""
解题思路:
这题很简单，但是要考虑怎样节省时间复杂度
基础解法双重循环: O(n^2)
当然我们可以调用python数组内置的方法原地删除，但是其实现原理是遍历一遍数组，找到要删除的元素，然后将其从数组中删除，时间复杂度为O(n)，那其实还增加了时间复杂度，只是因为其内置方法的实现是用C语言写的，所以速度快
若我们将baskets转化成链表，遍历fruits时，若当前fruit在baskets中，则将其从baskets中删除，时间复杂度为O(n*log(n))
"""
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # 将baskets转化成链表
        class Node:
            def __init__(self, value):
                self.value = value
                self.next = None

        pre_node = head = None
        for i in range(len(baskets)):
            _node = Node(baskets[i])
            if i == 0:
                head = _node
            if pre_node:
                pre_node.next = _node
            pre_node = _node

        suit = 0
        for fruit in fruits:
            _node = head
            _pre_node = None
            while _node:
                if fruit <= _node.value:
                    suit += 1
                    if not _pre_node:
                        head = _node.next
                    else:
                        _pre_node.next = _node.next
                    break

                _pre_node = _node
                _node = _node.next

        return len(fruits) - suit


if __name__ == '__main__':
    print(Solution().numOfUnplacedFruits([3, 6, 1], [3, 6, 4]))  # Example usage