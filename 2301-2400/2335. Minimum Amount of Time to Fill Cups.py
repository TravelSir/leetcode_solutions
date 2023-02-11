"""
解题思路:
这题很简单啊，就是尽量保证每次都能装两杯水，那么每次取需要装水次数最多和第二多的来装即可，
"""
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        cnt = 0
        while amount[0] > 0:
            amount[0] -= 1
            if amount[1]:
                amount[1] -= 1
            amount.sort(reverse=True)
            cnt += 1
        return cnt

