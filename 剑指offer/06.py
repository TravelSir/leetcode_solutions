"""
解题思路:
在不改变原链表下，新分配内存，从尾到头，也就是后进先出，用栈就可以实现
"""
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        vals = list()
        while head:
            vals.append(head.val)
            head = head.next

        return vals[::-1]

