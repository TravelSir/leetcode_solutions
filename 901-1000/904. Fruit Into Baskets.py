"""
解题思路:
因为要求采摘的顺序必须是连续的，且起点可以任选，那么可以使用滑动窗口的方式来解决这个问题。
滑动窗口的思路是维护一个窗口，窗口内的水果种类不超过两种。
我们可以使用两个指针来表示窗口的左右边界，左指针从0开始，右指针从0开始遍历数组。
当右指针指向的水果种类超过两种时，左指针向右移动，直到窗口内的水果种类不超过两种。
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        fruit_count = {}
        max_fruits = 0

        while right < len(fruits):
            fruit_count.setdefault(fruits[right], 0)
            fruit_count[fruits[right]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)
            right += 1

        return max_fruits
