"""
解题思路:
删除链表的倒数第n个节点，最简单能想到的是，遍历一遍链表，得到链表长度，然后再用链表长度减去n得到要删除的节点位置，再遍历到该节点位置进行删除。
这种方法要遍历两次，时间复杂度为O(2n)
但其实有只遍历一次的方法，有点类似滑动窗口，设定一个长度为n的子链表，从头开始往后移，当移动到末尾时，子链表的头节点就是倒数第n个节点。
当然我们这里要弄一个长度为n+1的子链表，因为要把倒数第n+1个节点和倒数n-1个节点接上
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head
        left = head
        right = head
        for i in range(n):
            right = right.next

        if right is None:
            head = head.next
            return head

        while right.next is not None:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head
