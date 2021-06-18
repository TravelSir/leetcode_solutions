"""
解题思路:
最简单的方法是遍历数组，但时间复杂度是O(n)。但好像跟是不是旋转数组没关系
所以我们需要利用好旋转数组的特性
首先旋转数组在旋转之前是一个递增数组，把开始的若干个元素搬到末尾，那么我们就可以用二分的思想
left为左边第一个元素，right为右边第一个元素，
我们就取数组中间数mid
- 如果mid<right, 说明最小数在左区间，right=mid
- 如果mid>right, 说明最小数在有区间，left=mid
- 如果mid=right，就无法判断最小数在哪个区间，假设最小值是right，因为mid=right，所以我们也可以忽略right，因为right的值是可以被mid替代的，所以right-=1
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1

        if right == -1:
            return None

        if right == 0:
            return numbers[0]

        while left < right - 1:
            mid = (right - left) // 2 + left

            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid
            else:
                right -= 1

        return numbers[left] if numbers[left] < numbers[right] else numbers[right]


if __name__ == '__main__':
    print(Solution().minArray([3, 3, 3, 1, 3, 3]))

