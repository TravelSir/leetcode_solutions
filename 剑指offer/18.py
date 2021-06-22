"""
解题思路:
删除链表中的一个节点，首先我们想到的就是从根节点遍历找到满足条件的节点删除，这种方式是顺序查找，时间复杂度为O(n)

其实原题的传参是两个ListNode节点，一个头节点，一个需要删除的子节点。要求的是在O(1)的时间内删除子节点。
用的方法是复制待删除节点的子节点值，再将带删除节点的子节点指向子节点的子节点，相当于转移删除了。
除了删除尾节点没有子节点需从头节点遍历正常删除，综合时间是O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        tem = head
        while tem.next:
            if tem.next.val == val:
                tem.next = tem.next.next
                break
            tem = tem.next
        return head
