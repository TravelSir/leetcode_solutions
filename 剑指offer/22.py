"""
解题思路:
因为不知道链表的长度，所以只能遍历完链表才能确定倒数第k个节点。
那我们第一次遍历n次，能确定链表的长度。
第二次遍历n-k次，就能确定倒数第k个节点

那我们不如将两次遍历合成一次，使用快慢指针，快指针比慢指针多k步。这样就能在O(n)的时间找到倒数k节点
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head
        while fast and k:
            fast = fast.next
            k -= 1

        if k > 0:
            return None

        while fast:
            fast = fast.next
            slow = slow.next

        return slow

