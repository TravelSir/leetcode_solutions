"""
解题思路:
要使时间复杂度在O(nlog(n))，这里就要使用分治法中的归并排序思想
最复杂也是最精妙得一步就是为了实现空间复杂度为常量级，那就得操作自身链表，自底向上的合并排序链表
首先第一步，我们就是要将第1和第2个节点合并排序，第3和第4个节点合并排序，以此类推直到链表结束
第二步，就是要将之前合并的12节点和34节点合并排序。。。
。。。
一直如此直到合并完成

那么问题来了，我们如何知道该合并哪两个排序后的小链表呢
其实在第一步时，每个节点只要依次遍历即可
在第二步时，合并后的子链表的头节点在之间的距离是1
在第三步时，合并后的子链表的头节点在之间的距离是3
这就说明
第一步时，把第一个节点作为左子表的头节点，右子表的头节点就等于第一个节点+1，下一个左子表的头节点等于上一个右子表的头节点+1
第二步时，把第一个节点作为左子表的头节点，右子表的头节点就等于第一个节点+2，下一个左子表的头节点等于上一个右子表的头节点+2
第三步时，把第一个节点作为左子表的头节点，右子表的头节点就等于第一个节点+4，下一个左子表的头节点等于上一个右子表的头节点+4
。。。
其实每个子链表之间的距离就是合并后的子链表的长度也就是2的n次方，那么当子链表长度大于等于总链表的长度时就代表排序完成了

如何合并排序两个链表呢
这个时候我们需要一个临时节点，初始是指向第一个节点的，这样归并排序就以这个临时节点来作为合并后的头节点。因为为了使空间复杂度为常量，我们要尽量操作自身
所以交换时不能新建一个空间来存，需要交换自身节点，所以我们需要确定左右子表头节点的父节点，这样在交换头节点时才能将对应父节点的指向也改变。
而这个临时节点在每一次比较的时候都指向子表的头节点
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

    def sortList(self, head):
        if not head or not head.next:
            return head

        lens = 0
        # 第一次遍历记录链表总长度
        _head = head
        while _head:
            _head = _head.next
            lens += 1

        # 已经自底向上合并排序过一次了，所以子链表长度从2开始
        _len = 1
        tem = ListNode(0)
        tem.next = head
        while _len < lens:
            _head = tem.next
            tem_l = tem
            while _head:
                len_left = _len
                left, i = _head, _len
                while i and _head:
                    _head = _head.next
                    i -= 1
                if i:
                    break

                right = _head
                len_right = 0
                while len_right < _len and _head:
                    _head = _head.next
                    len_right += 1

                while len_left and len_right:
                    if left.val <= right.val:
                        tem_l.next = left
                        left = left.next
                        len_left -= 1
                    else:
                        tem_l.next = right
                        right = right.next
                        len_right -= 1
                    tem_l = tem_l.next
                if len_left:
                    tem_l.next = left
                if len_right:
                    tem_l.next = right
                while len_left > 0 or len_right > 0:
                    len_left -= 1
                    len_right -= 1
                    tem_l = tem_l.next
                tem_l.next = _head

            _len *= 2

        return tem.next


if __name__ == '__main__':
    link = ListNode(-1)
    link.make_node([-84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115])
    print(Solution().sortList(link))
