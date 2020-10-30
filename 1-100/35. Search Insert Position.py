"""
解题思路:
很基础的一题了，二分查找法
"""


class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid - 1

        return left if nums and nums[left] >= target else (left + 1)


if __name__ == '__main__':
    print(Solution().searchInsert([1], 0))
