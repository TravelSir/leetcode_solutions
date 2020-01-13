"""
解题思路:
因为是以逆序存储，所以链表头节点一定是个位数，以此类推
所以这题很简单，两个链表同时从头节点遍历，两值相加并加上初始化的up，up变量记录是否进1，up初始为0
为了节约内存，我们可以以第一个链表作为结果表存上每次计算的结果，
还有一种特殊情况，就是最后一位结果进1了，需要新建一个链表节点, 若要节约内存就直接指向第二个链表头，将其值改为1，再指向null
"""


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
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        head1 = l1
        head2 = l2
        up = 0
        res = head1

        while head1 or head2:
            _sum = 0
            if head1:
                _sum += head1.val
                head1 = head1.next
                if head1:
                    res.next = head1
                elif head2 and head2.next:
                    res.next = head2.next

            if head2:
                _sum += head2.val
                head2 = head2.next

            _sum += up
            if _sum >= 10:
                up = 1
                _sum -= 10
            else:
                up = 0

            res.val = _sum
            if res.next:
                res = res.next

        if up:
            l2.val = 1
            l2.next = None
            res.next = l2

        return l1


if __name__ == '__main__':
    l1 = ListNode(2)
    l2 = ListNode(1)
    l1.make_node([4])
    l2.make_node([6, 4])
    print(l1, l2, sep='\n')
    print(Solution().addTwoNumbers(l1, l2))
