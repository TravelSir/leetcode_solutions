"""
解题思路:
要求三数之和最接近target，最暴力的解法就是直接三层循环，时间复杂度为O(n*n*n)
若我们将数组排序后以第一个数为基数n,右区间的左边界为a，有边界为b
若n+a+b<target, 说明a+b需更大，若移动b就只会让和更小，所以b不能动，a需右移动
若n+a+b>target, 说明a+b需更小，若移动a就只会让和更大，所以a不能动，b需左移动
当n+a+b=target时则直接返回

一个优化：
在每次移动基准数的时候，判断基准数向右的连续三数之和是否大于target,若大于则不再循环，直接判断
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(length - 2):
            judge = nums[i] + nums[i+1] + nums[i+2]
            if judge > target:
                return result if abs(result - target) < abs(judge - target) else judge
            j = i + 1
            k = length - 1
            while j < k:
                tem = nums[i] + nums[j] + nums[k]
                if tem == target:
                    return tem
                elif tem < target:
                    j += 1
                else:
                    k -= 1
                if abs(result - target) > abs(tem - target):
                    result = tem
        return result


if __name__ == '__main__':
    nums = [1, 1, -1, -1, 3]
    target = -1
    print(Solution().threeSumClosest(nums, target))

