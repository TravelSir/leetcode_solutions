"""
解题思路:
要将链表反转，我们可以使用一个中间节点指针mid，初始化为None.
每次遍历节点head时，用一个临时变量tem指针指向head的子节点，然后将head的子节点指向mid，mid节点指针再指向head节点，最后head指针再指向tem指针。就完成了交换
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        mid = None
        if not head:
            return head
        while head:
            tem = head.next
            head.next = mid
            mid = head
            head = tem
        return mid

