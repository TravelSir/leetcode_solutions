"""
解题思路:
最简单的思路就是，遍历一次链表，依次判断节点是否在数组内。可以将数组转化成哈希表，这样时间复杂度和空间复杂度都是O(n)
"""


from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_dict = {n: 1 for n in nums}
        count = tem = 0
        while head:
            if num_dict.get(head.val):
                tem += 1
            else:
                if tem > 0:
                    count += 1
                tem = 0
            head = head.next
        if tem > 0:
            count += 1
        return count


if __name__ == '__main__':
    head = ListNode()
    print(Solution().numComponents(head, [0]))