"""
解题思路:
子数组要求元素互不相同，且原数组可以随意删除元素，且求子数组最大和，那其实代表的就是原数组首先去重，然后再删除小于0的元素，最后求和。
但有个特殊情况是子数组不能为空，那么如果原数组全是负数，那么就只能返回最大的负数。

考虑到时间复杂度，尽量一次遍历完成去重和求值。虽然用内置方法set()更快，但是实际从时间复杂来说是用O(2n)。
所以这里还是用一次遍历，用一个值记录最大数。小于0的数不用于算和。
用nums_map用于标记是否重复,不用list是为了节约时间。
最后的返回，如果max_sum=0则代表数组全为非正数，则返回max_num最大非正数即可

"""
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_num = nums[0]
        max_sum = 0
        nums_map = dict()
        for num in nums:
            max_num = max(max_num, num)
            if num < 0:
                continue
            if num in nums_map:
                continue
            nums_map[num] = True
            max_sum += num

        return max_sum or max_num


if __name__ == '__main__':
    print(Solution().maxSum([-17, -15]))  # Example usage

