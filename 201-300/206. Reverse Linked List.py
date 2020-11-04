"""
解题思路:
反转链表可以一次遍历就实现，left = 头节点, right = 第二个节点， tem = 第三个节点
第一个节点的next指向null，将第二个节点的next指向第一个节点，判断tem是否为null，tem为null则反转完成, 此时right为头指针
否则，left = right, right = tem, tem = right.next，继续循环判断

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
    def reverseList(self, head):
        left = head
        if left is None:
            return head

        right = left.next
        if right is None:
            return head

        left.next = None

        while right:
            tem = right.next
            right.next = left
            if tem is None:
                break
            left = right
            right = tem
        return right


if __name__ == '__main__':
    a = [1,2]
    l = ListNode(a[0])
    l.make_node(a[1:])
    print(l)
    print(Solution().reverseList(l))
