"""
解题思路:
四数之和, 首先使用暴力四层循环的时间复杂度太高，为O(n^4),
那我们可以将数组进行排序，将前两层循环当作一个整体数，按照三数之和的方式，使用双指针指向数组后的前后两端。
这样可以降低一次循环，时间复杂度为O(n^3)。
当然我们还可以进行一些剪枝操作（实际意义不大，只能针对个别无解或少解用例）:
1.当排序后的前四个数和大于target时，可直接返回。
2.当排序后的第一个数和倒数三个数之和小于target时，可直接返回。
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lens = len(nums)
        res = []
        for i in range(0, lens - 3):
            for j in range(i + 1, lens - 2):
                pre_sum = nums[i] + nums[j]
                left = j + 1
                right = lens - 1
                while left < right:
                    if pre_sum + nums[left] + nums[right] == target:
                        tem = [nums[i], nums[j], nums[left], nums[right]]
                        left += 1
                        right -= 1
                        if tem in res:
                            continue
                        res.append(tem)
                    elif pre_sum + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(Solution().fourSum(nums, target))
