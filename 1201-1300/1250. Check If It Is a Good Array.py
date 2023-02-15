"""
解题思路:
这是一道数学题，裴蜀定理。说实话自己证明了半天没证出来。其实就是求两数最大公约数。这也是数学题
python的math库提供了gcd方法求最大公约数。然后将公约数依次比较即可。这题考数学- -
"""
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1

