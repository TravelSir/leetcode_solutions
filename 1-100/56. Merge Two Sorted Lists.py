"""
解题思路:
合并两个有序链表很简单，我们可以用双指针，始终都是小的指针往后移动，当某一个指针指向空时，则排序结束，只需一次遍历，时间复杂度是O(m+n)
这题我们为了节省空间，先确定head，然后判断两链表值大小, 然后使用_head初始化等于head来每次往后移动到更小的那根链表上去
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def make_node(self, array):
        l = self
        for i in array:
            tem = ListNode(i)
            l.next = tem
            l = tem

    def __repr__(self):
        l = self
        _str = []
        while l:
            _str.append(str(l.val))
            l = l.next
        return ' '.join(_str)


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        # 确定拼接后的链表头节点
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        _head = head

        while l1 and l2:
            if l1.val <= l2.val:
                _head.next = l1
                l1 = l1.next
            else:
                _head.next = l2
                l2 = l2.next
            _head = _head.next
            # print(_head, l1, l2, sep=' | ')
        if l1:
            _head.next = l1
        if l2:
            _head.next = l2

        return head


if __name__ == '__main__':
    a = [1, 2, 4]
    b = [1, 3, 4]
    l1 = ListNode(a[0])
    l2 = ListNode(b[0])
    l1.make_node(a[1:])
    l2.make_node(b[1:])
    print(l1, l2, sep='\n')

    print(Solution().mergeTwoLists(l1, None))
