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

这里有个情况是，当left < right的时候，那肯定已经是有序了，最小值就肯定是left
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if right == -1:
            return None

        if right == 0:
            return nums[0]

        while left < right - 1:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (right - left) // 2 + left

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right -= 1

        return nums[left] if nums[left] < nums[right] else nums[right]

