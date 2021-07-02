"""
解题思路:
利用贪心思想来分析，要多买雪糕，应该是越便宜的越买。
第一种方法是快排之后来计算，时间复杂度为O(n*log(n)+n)
第二种是计数排序，空间和时间复杂度都是O(n+k), k为整数范围
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        num = 0
        for c in costs:
            coins -= c
            if coins >= 0:
                num += 1
            else:
                break
        return num

    def count_sort(self, costs: List[int], coins: int) -> int:
        num = 0
        count_costs = [0] * 100000
        for c in costs:
            count_costs[c-1] += 1

        for i in range(100000):
            while count_costs[i]:
                coins -= i + 1
                count_costs[i] -= 1
                if coins >= 0:
                    num += 1
                else:
                    return num

        return num

