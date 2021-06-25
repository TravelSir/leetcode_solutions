"""
解题思路:
合并两个递增排序的链表，思路和合并两个递增数组差不多，就是要注意链表合并后的指向问题
当然最简单的方法就是新建一个链表来存储，消耗O(n)的空间和O(n)的时间。
但我们要学会原地合并, 首先我们得确认合并到哪个链上
首先有两个指针ah,bh 分别指向两个链表的头节点。比较ah，bh指针的值，
如果ah指针的值小于bh指针的值， 说明ah指针要合并在bh指针之前，但不能立即合并，因为可能ah后面的指针依旧小于bh指针
这时候需有一个ac指针指向ah的子节点，判断ac与bh的大小，如果ac<=bh,则ac继续指向子节点，直到ac指向None或者ac>bh，ac指向bh，ah等于ac之前的子节点
如此循换，直到ah或bh为None
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        ah = l1
        bh = l2
        while ah and bh:
            if ah.val >= bh.val:
                ah, bh = bh, ah
            ac = ah
            while ac.next and ac.next.val <= bh.val:
                ac = ac.next
            tem = ac.next
            ac.next = bh
            ah = tem

        return l1 if l1.val < l2.val else l2


if __name__ == '__main__':
    print(Solution().mergeTwoLists(ListNode(2), ListNode(1)))

