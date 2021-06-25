"""
解题思路:
这题我们可以用双指针来做，左指针从头部开始，标记奇数的边界，右指针从尾部开始，标记偶数的边界
当左指针指向的数为奇数时，则右移一位。
当左指针指向的数为偶数时，则交换左右指针的数，右指针左移一位
直到左右指针重合, 这个题的时间复杂度是O(n)
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] & 1:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return nums

