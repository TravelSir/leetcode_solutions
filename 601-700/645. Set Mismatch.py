"""
解题思路:
最简单的做法就是快排一次，然后顺序查找重复和缺失的数
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        tem, repeate, miss = nums[0], 0, 0
        for n in nums[1:]:
            if n == tem:
                repeate = tem
            elif tem + 1 != n:
                miss = tem + 1
            if repeate and miss:
                break
            tem = n
        if nums[0] != 1:
            miss = 1
        if not miss:
            miss = tem + 1
        return [repeate, miss]


if __name__ == '__main__':
    print(Solution().findErrorNums([1,3,3]))

