"""
解题思路:
第一种办法是 快排+单次遍历，时间复杂度为O(nlog(n)), 空间复杂度为O(1)
第二种办法是 用哈希表存储，单次遍历, 时间复杂度为O(n), 空间复杂度为O(n)
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = dict()
        for n in nums:
            if n in num_dict:
                return True
            num_dict[n] = 1
        return False
